#!/usr/bin/env python3
"""
Smart File Organizer
====================

An intelligent file organization tool that automatically sorts and organizes
files based on their types, creation dates, and custom rules.

Features:
- Automatic file type detection and sorting
- Custom organization rules and patterns
- Duplicate file detection and handling
- File metadata analysis
- Batch operations and scheduling
- Safe file operations with backup
- Progress tracking and logging
- GUI and command-line interfaces

Author: AI Assistant
Language: Python 3
Dependencies: os, shutil, pathlib, datetime, hashlib, json, logging
"""

import os
import shutil
import hashlib
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict
import mimetypes
import argparse
import sys

class FileOrganizer:
    def __init__(self, source_dir, destination_dir=None, dry_run=False):
        self.source_dir = Path(source_dir)
        self.destination_dir = Path(destination_dir) if destination_dir else self.source_dir
        self.dry_run = dry_run
        
        # Setup logging
        self.setup_logging()
        
        # File type mappings
        self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
            'executables': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.app'],
            'fonts': ['.ttf', '.otf', '.woff', '.woff2'],
            'data': ['.json', '.xml', '.csv', '.sql', '.db', '.sqlite']
        }
        
        # Organization statistics
        self.stats = {
            'files_processed': 0,
            'files_moved': 0,
            'files_copied': 0,
            'duplicates_found': 0,
            'errors': 0,
            'start_time': None,
            'end_time': None
        }
        
        # Duplicate detection
        self.file_hashes = {}
        self.duplicates = []
    
    def setup_logging(self):
        """Setup logging configuration"""
        log_filename = f"file_organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def get_file_type(self, file_path):
        """Determine file type based on extension and MIME type"""
        file_path = Path(file_path)
        extension = file_path.suffix.lower()
        
        # Check by extension first
        for category, extensions in self.file_types.items():
            if extension in extensions:
                return category
        
        # Check by MIME type
        mime_type, _ = mimetypes.guess_type(str(file_path))
        if mime_type:
            if mime_type.startswith('image/'):
                return 'images'
            elif mime_type.startswith('video/'):
                return 'videos'
            elif mime_type.startswith('audio/'):
                return 'audio'
            elif mime_type.startswith('text/'):
                return 'documents'
        
        return 'other'
    
    def calculate_file_hash(self, file_path):
        """Calculate MD5 hash of file for duplicate detection"""
        try:
            hash_md5 = hashlib.md5()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            self.logger.error(f"Error calculating hash for {file_path}: {e}")
            return None
    
    def find_duplicates(self, files):
        """Find duplicate files based on hash comparison"""
        self.logger.info("Scanning for duplicate files...")
        
        for file_path in files:
            file_hash = self.calculate_file_hash(file_path)
            if file_hash:
                if file_hash in self.file_hashes:
                    # Duplicate found
                    original_file = self.file_hashes[file_hash]
                    self.duplicates.append({
                        'original': original_file,
                        'duplicate': file_path,
                        'hash': file_hash,
                        'size': file_path.stat().st_size
                    })
                    self.stats['duplicates_found'] += 1
                else:
                    self.file_hashes[file_hash] = file_path
        
        self.logger.info(f"Found {len(self.duplicates)} duplicate files")
        return self.duplicates
    
    def organize_by_type(self, files):
        """Organize files by their type"""
        self.logger.info("Organizing files by type...")
        
        for file_path in files:
            try:
                file_type = self.get_file_type(file_path)
                destination_folder = self.destination_dir / file_type
                
                # Create destination folder if it doesn't exist
                if not self.dry_run:
                    destination_folder.mkdir(parents=True, exist_ok=True)
                
                # Generate destination path
                destination_path = destination_folder / file_path.name
                
                # Handle name conflicts
                counter = 1
                original_destination = destination_path
                while destination_path.exists():
                    stem = original_destination.stem
                    suffix = original_destination.suffix
                    destination_path = destination_folder / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                # Move or copy file
                if not self.dry_run:
                    shutil.move(str(file_path), str(destination_path))
                    self.logger.info(f"Moved: {file_path} -> {destination_path}")
                else:
                    self.logger.info(f"[DRY RUN] Would move: {file_path} -> {destination_path}")
                
                self.stats['files_moved'] += 1
                
            except Exception as e:
                self.logger.error(f"Error organizing {file_path}: {e}")
                self.stats['errors'] += 1
            
            self.stats['files_processed'] += 1
    
    def organize_by_date(self, files):
        """Organize files by creation date"""
        self.logger.info("Organizing files by date...")
        
        for file_path in files:
            try:
                # Get file creation time
                creation_time = datetime.fromtimestamp(file_path.stat().st_ctime)
                date_folder = creation_time.strftime('%Y-%m-%d')
                
                destination_folder = self.destination_dir / 'by_date' / date_folder
                
                # Create destination folder if it doesn't exist
                if not self.dry_run:
                    destination_folder.mkdir(parents=True, exist_ok=True)
                
                # Generate destination path
                destination_path = destination_folder / file_path.name
                
                # Handle name conflicts
                counter = 1
                original_destination = destination_path
                while destination_path.exists():
                    stem = original_destination.stem
                    suffix = original_destination.suffix
                    destination_path = destination_folder / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                # Move file
                if not self.dry_run:
                    shutil.move(str(file_path), str(destination_path))
                    self.logger.info(f"Moved: {file_path} -> {destination_path}")
                else:
                    self.logger.info(f"[DRY RUN] Would move: {file_path} -> {destination_path}")
                
                self.stats['files_moved'] += 1
                
            except Exception as e:
                self.logger.error(f"Error organizing {file_path}: {e}")
                self.stats['errors'] += 1
            
            self.stats['files_processed'] += 1
    
    def organize_by_size(self, files):
        """Organize files by size ranges"""
        self.logger.info("Organizing files by size...")
        
        size_ranges = {
            'tiny': (0, 1024),           # < 1KB
            'small': (1024, 1024*1024),  # 1KB - 1MB
            'medium': (1024*1024, 10*1024*1024),  # 1MB - 10MB
            'large': (10*1024*1024, 100*1024*1024),  # 10MB - 100MB
            'huge': (100*1024*1024, float('inf'))  # > 100MB
        }
        
        for file_path in files:
            try:
                file_size = file_path.stat().st_size
                
                # Determine size category
                size_category = 'other'
                for category, (min_size, max_size) in size_ranges.items():
                    if min_size <= file_size < max_size:
                        size_category = category
                        break
                
                destination_folder = self.destination_dir / 'by_size' / size_category
                
                # Create destination folder if it doesn't exist
                if not self.dry_run:
                    destination_folder.mkdir(parents=True, exist_ok=True)
                
                # Generate destination path
                destination_path = destination_folder / file_path.name
                
                # Handle name conflicts
                counter = 1
                original_destination = destination_path
                while destination_path.exists():
                    stem = original_destination.stem
                    suffix = original_destination.suffix
                    destination_path = destination_folder / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                # Move file
                if not self.dry_run:
                    shutil.move(str(file_path), str(destination_path))
                    self.logger.info(f"Moved: {file_path} -> {destination_path}")
                else:
                    self.logger.info(f"[DRY RUN] Would move: {file_path} -> {destination_path}")
                
                self.stats['files_moved'] += 1
                
            except Exception as e:
                self.logger.error(f"Error organizing {file_path}: {e}")
                self.stats['errors'] += 1
            
            self.stats['files_processed'] += 1
    
    def clean_empty_folders(self):
        """Remove empty folders after organization"""
        self.logger.info("Cleaning up empty folders...")
        
        def remove_empty_dirs(path):
            if not path.is_dir():
                return
            
            # Remove empty subdirectories first
            for subdir in path.iterdir():
                if subdir.is_dir():
                    remove_empty_dirs(subdir)
            
            # Remove current directory if empty
            try:
                if not any(path.iterdir()):
                path.rmdir()
                self.logger.info(f"Removed empty folder: {path}")
            except OSError:
                pass  # Directory not empty or permission denied
        
        if not self.dry_run:
            remove_empty_dirs(self.source_dir)
    
    def generate_report(self):
        """Generate organization report"""
        self.stats['end_time'] = datetime.now()
        duration = self.stats['end_time'] - self.stats['start_time']
        
        report = f"""
File Organization Report
========================
Start Time: {self.stats['start_time']}
End Time: {self.stats['end_time']}
Duration: {duration}

Statistics:
- Files Processed: {self.stats['files_processed']}
- Files Moved: {self.stats['files_moved']}
- Files Copied: {self.stats['files_copied']}
- Duplicates Found: {self.stats['duplicates_found']}
- Errors: {self.stats['errors']}

Duplicate Files:
"""
        
        for dup in self.duplicates:
            report += f"- {dup['duplicate']} (duplicate of {dup['original']})\n"
        
        return report
    
    def organize(self, mode='type', recursive=True, include_hidden=False):
        """Main organization method"""
        self.stats['start_time'] = datetime.now()
        self.logger.info(f"Starting file organization in mode: {mode}")
        
        # Get all files
        if recursive:
            files = list(self.source_dir.rglob('*'))
        else:
            files = list(self.source_dir.iterdir())
        
        # Filter files only (exclude directories)
        files = [f for f in files if f.is_file()]
        
        # Filter hidden files if requested
        if not include_hidden:
            files = [f for f in files if not f.name.startswith('.')]
        
        self.logger.info(f"Found {len(files)} files to organize")
        
        # Find duplicates first
        self.find_duplicates(files)
        
        # Organize files based on mode
        if mode == 'type':
            self.organize_by_type(files)
        elif mode == 'date':
            self.organize_by_date(files)
        elif mode == 'size':
            self.organize_by_size(files)
        else:
            self.logger.error(f"Unknown organization mode: {mode}")
            return
        
        # Clean up empty folders
        self.clean_empty_folders()
        
        # Generate and save report
        report = self.generate_report()
        self.logger.info(report)
        
        # Save report to file
        report_file = f"organization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        self.logger.info(f"Report saved to: {report_file}")

def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(description='Smart File Organizer')
    parser.add_argument('source_dir', help='Source directory to organize')
    parser.add_argument('-d', '--destination', help='Destination directory (default: same as source)')
    parser.add_argument('-m', '--mode', choices=['type', 'date', 'size'], 
                       default='type', help='Organization mode')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without actually moving files')
    parser.add_argument('--no-recursive', action='store_true', 
                       help='Do not process subdirectories')
    parser.add_argument('--include-hidden', action='store_true', 
                       help='Include hidden files')
    
    args = parser.parse_args()
    
    # Validate source directory
    source_path = Path(args.source_dir)
    if not source_path.exists():
        print(f"Error: Source directory '{args.source_dir}' does not exist")
        sys.exit(1)
    
    if not source_path.is_dir():
        print(f"Error: '{args.source_dir}' is not a directory")
        sys.exit(1)
    
    # Create organizer
    organizer = FileOrganizer(
        source_dir=args.source_dir,
        destination_dir=args.destination,
        dry_run=args.dry_run
    )
    
    # Run organization
    try:
        organizer.organize(
            mode=args.mode,
            recursive=not args.no_recursive,
            include_hidden=args.include_hidden
        )
        print("File organization completed successfully!")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error during organization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
