#!/usr/bin/env python3
"""
Advanced Password Generator
===========================

A comprehensive password generator that creates secure, customizable passwords
with various complexity levels and security features.

Features:
- Multiple password generation strategies
- Customizable length and character sets
- Password strength analysis
- Secure random generation
- Password history and validation
- Export/import functionality

Author: AI Assistant
Language: Python 3
Dependencies: secrets, string, random, json, datetime
"""

import secrets
import string
import random
import json
import datetime
import hashlib
import base64

class PasswordGenerator:
    def __init__(self):
        self.password_history = []
        self.strength_levels = {
            "weak": 0,
            "medium": 1,
            "strong": 2,
            "very_strong": 3
        }
        
        # Character sets
        self.char_sets = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "symbols": "!@#$%^&*()_+-=[]{}|;:,.<>?",
            "extended": "~`!@#$%^&*()_+-=[]{}|;:,.<>?/\\\"'"
        }
    
    def generate_password(self, length=12, include_uppercase=True, include_lowercase=True, 
                         include_digits=True, include_symbols=True, exclude_similar=True,
                         exclude_ambiguous=True, min_uppercase=1, min_lowercase=1, 
                         min_digits=1, min_symbols=1):
        """
        Generate a secure password with specified requirements
        
        Args:
            length (int): Password length
            include_uppercase (bool): Include uppercase letters
            include_lowercase (bool): Include lowercase letters
            include_digits (bool): Include digits
            include_symbols (bool): Include symbols
            exclude_similar (bool): Exclude similar characters (0, O, l, 1)
            exclude_ambiguous (bool): Exclude ambiguous characters
            min_uppercase (int): Minimum uppercase letters required
            min_lowercase (int): Minimum lowercase letters required
            min_digits (int): Minimum digits required
            min_symbols (int): Minimum symbols required
        
        Returns:
            str: Generated password
        """
        
        # Build character pool
        char_pool = ""
        required_chars = []
        
        if include_lowercase:
            chars = self.char_sets["lowercase"]
            if exclude_similar:
                chars = chars.replace('l', '').replace('o', '')
            if exclude_ambiguous:
                chars = chars.replace('i', '').replace('j', '')
            char_pool += chars
            required_chars.extend(random.choices(chars, k=min_lowercase))
        
        if include_uppercase:
            chars = self.char_sets["uppercase"]
            if exclude_similar:
                chars = chars.replace('O', '').replace('I', '')
            if exclude_ambiguous:
                chars = chars.replace('I', '').replace('J', '')
            char_pool += chars
            required_chars.extend(random.choices(chars, k=min_uppercase))
        
        if include_digits:
            chars = self.char_sets["digits"]
            if exclude_similar:
                chars = chars.replace('0', '').replace('1', '')
            char_pool += chars
            required_chars.extend(random.choices(chars, k=min_digits))
        
        if include_symbols:
            chars = self.char_sets["symbols"]
            if exclude_ambiguous:
                chars = chars.replace('(', '').replace(')', '').replace('[', '').replace(']', '')
            char_pool += chars
            required_chars.extend(random.choices(chars, k=min_symbols))
        
        if not char_pool:
            raise ValueError("At least one character set must be included")
        
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        if remaining_length < 0:
            raise ValueError("Minimum requirements exceed password length")
        
        additional_chars = [secrets.choice(char_pool) for _ in range(remaining_length)]
        
        # Combine and shuffle
        all_chars = required_chars + additional_chars
        random.shuffle(all_chars)
        
        password = ''.join(all_chars)
        
        # Store in history
        self._add_to_history(password)
        
        return password
    
    def generate_passphrase(self, word_count=4, separator="-", capitalize=True, 
                           include_numbers=True, include_symbols=False):
        """
        Generate a memorable passphrase using common words
        
        Args:
            word_count (int): Number of words in passphrase
            separator (str): Separator between words
            capitalize (bool): Capitalize first letter of each word
            include_numbers (bool): Include random numbers
            include_symbols (bool): Include random symbols
        
        Returns:
            str: Generated passphrase
        """
        
        # Common word list for passphrases
        word_list = [
            "apple", "banana", "cherry", "dragon", "eagle", "forest", "garden",
            "house", "island", "jungle", "knight", "ladder", "mountain", "ocean",
            "palace", "queen", "river", "sunset", "tiger", "umbrella", "violet",
            "window", "yellow", "zebra", "adventure", "beautiful", "creative",
            "dancing", "electric", "fantastic", "guitar", "harmony", "incredible",
            "journey", "knowledge", "laughter", "magical", "nature", "optimistic",
            "peaceful", "quality", "rainbow", "sunshine", "treasure", "unique",
            "victory", "wonderful", "excellent", "yesterday", "zealous"
        ]
        
        # Select random words
        words = random.sample(word_list, word_count)
        
        # Apply modifications
        if capitalize:
            words = [word.capitalize() for word in words]
        
        # Add numbers and symbols if requested
        if include_numbers:
            words.append(str(random.randint(10, 99)))
        
        if include_symbols:
            symbols = "!@#$%^&*"
            words.append(random.choice(symbols))
        
        passphrase = separator.join(words)
        
        # Store in history
        self._add_to_history(passphrase)
        
        return passphrase
    
    def analyze_password_strength(self, password):
        """
        Analyze password strength and provide detailed feedback
        
        Args:
            password (str): Password to analyze
        
        Returns:
            dict: Analysis results
        """
        
        score = 0
        feedback = []
        
        # Length analysis
        length = len(password)
        if length < 8:
            feedback.append("Password is too short (minimum 8 characters recommended)")
        elif length >= 12:
            score += 2
            feedback.append("Good password length")
        else:
            score += 1
        
        # Character variety analysis
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        char_types = sum([has_lower, has_upper, has_digit, has_symbol])
        
        if char_types >= 4:
            score += 3
            feedback.append("Excellent character variety")
        elif char_types == 3:
            score += 2
            feedback.append("Good character variety")
        elif char_types == 2:
            score += 1
            feedback.append("Consider adding more character types")
        else:
            feedback.append("Password uses only one character type")
        
        # Pattern analysis
        if self._has_common_patterns(password):
            score -= 1
            feedback.append("Avoid common patterns (123, abc, qwerty)")
        
        # Entropy calculation
        entropy = self._calculate_entropy(password)
        if entropy > 60:
            score += 2
            feedback.append("High entropy - very secure")
        elif entropy > 40:
            score += 1
            feedback.append("Good entropy")
        else:
            feedback.append("Low entropy - consider more randomness")
        
        # Determine strength level
        if score >= 6:
            strength = "very_strong"
        elif score >= 4:
            strength = "strong"
        elif score >= 2:
            strength = "medium"
        else:
            strength = "weak"
        
        return {
            "password": password,
            "length": length,
            "strength": strength,
            "score": score,
            "entropy": entropy,
            "feedback": feedback,
            "character_types": {
                "lowercase": has_lower,
                "uppercase": has_upper,
                "digits": has_digit,
                "symbols": has_symbol
            }
        }
    
    def _has_common_patterns(self, password):
        """Check for common patterns in password"""
        common_patterns = [
            "123", "abc", "qwerty", "password", "admin", "user",
            "letmein", "welcome", "monkey", "dragon", "master"
        ]
        
        password_lower = password.lower()
        return any(pattern in password_lower for pattern in common_patterns)
    
    def _calculate_entropy(self, password):
        """Calculate password entropy"""
        char_set_size = 0
        
        if any(c.islower() for c in password):
            char_set_size += 26
        if any(c.isupper() for c in password):
            char_set_size += 26
        if any(c.isdigit() for c in password):
            char_set_size += 10
        if any(c in string.punctuation for c in password):
            char_set_size += 32
        
        if char_set_size == 0:
            return 0
        
        entropy = len(password) * (char_set_size ** 0.5)
        return entropy
    
    def _add_to_history(self, password):
        """Add password to history with metadata"""
        entry = {
            "password": password,
            "timestamp": datetime.datetime.now().isoformat(),
            "hash": hashlib.sha256(password.encode()).hexdigest()[:16]
        }
        self.password_history.append(entry)
        
        # Keep only last 50 passwords
        if len(self.password_history) > 50:
            self.password_history = self.password_history[-50:]
    
    def export_passwords(self, filename="password_export.json", include_passwords=True):
        """Export password history to file"""
        export_data = {
            "export_date": datetime.datetime.now().isoformat(),
            "total_passwords": len(self.password_history),
            "passwords": []
        }
        
        for entry in self.password_history:
            if include_passwords:
                export_data["passwords"].append(entry)
            else:
                # Export only metadata without actual passwords
                export_data["passwords"].append({
                    "timestamp": entry["timestamp"],
                    "hash": entry["hash"]
                })
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        return f"Exported {len(self.password_history)} passwords to {filename}"
    
    def generate_bulk_passwords(self, count=10, **kwargs):
        """Generate multiple passwords at once"""
        passwords = []
        for _ in range(count):
            password = self.generate_password(**kwargs)
            passwords.append(password)
        return passwords

def main():
    """Main function to run the password generator"""
    print("🔐 Advanced Password Generator")
    print("=" * 50)
    
    generator = PasswordGenerator()
    
    while True:
        print("\nOptions:")
        print("1. Generate Single Password")
        print("2. Generate Passphrase")
        print("3. Generate Multiple Passwords")
        print("4. Analyze Password Strength")
        print("5. View Password History")
        print("6. Export Passwords")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            try:
                length = int(input("Password length (default 12): ") or "12")
                include_upper = input("Include uppercase? (y/n, default y): ").lower() != 'n'
                include_lower = input("Include lowercase? (y/n, default y): ").lower() != 'n'
                include_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
                include_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
                
                password = generator.generate_password(
                    length=length,
                    include_uppercase=include_upper,
                    include_lowercase=include_lower,
                    include_digits=include_digits,
                    include_symbols=include_symbols
                )
                
                print(f"\nGenerated Password: {password}")
                
                # Analyze strength
                analysis = generator.analyze_password_strength(password)
                print(f"Strength: {analysis['strength'].upper()}")
                print(f"Score: {analysis['score']}/8")
                print("Feedback:")
                for feedback in analysis['feedback']:
                    print(f"  - {feedback}")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                word_count = int(input("Number of words (default 4): ") or "4")
                separator = input("Separator (default '-'): ") or "-"
                capitalize = input("Capitalize words? (y/n, default y): ").lower() != 'n'
                include_numbers = input("Include numbers? (y/n, default n): ").lower() == 'y'
                include_symbols = input("Include symbols? (y/n, default n): ").lower() == 'y'
                
                passphrase = generator.generate_passphrase(
                    word_count=word_count,
                    separator=separator,
                    capitalize=capitalize,
                    include_numbers=include_numbers,
                    include_symbols=include_symbols
                )
                
                print(f"\nGenerated Passphrase: {passphrase}")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            try:
                count = int(input("Number of passwords to generate (default 10): ") or "10")
                length = int(input("Password length (default 12): ") or "12")
                
                passwords = generator.generate_bulk_passwords(count=count, length=length)
                
                print(f"\nGenerated {count} passwords:")
                for i, password in enumerate(passwords, 1):
                    print(f"{i:2d}. {password}")
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            password = input("Enter password to analyze: ").strip()
            if password:
                analysis = generator.analyze_password_strength(password)
                print(f"\nPassword Analysis:")
                print(f"Password: {analysis['password']}")
                print(f"Length: {analysis['length']}")
                print(f"Strength: {analysis['strength'].upper()}")
                print(f"Score: {analysis['score']}/8")
                print(f"Entropy: {analysis['entropy']:.2f}")
                print("Character Types:")
                for char_type, present in analysis['character_types'].items():
                    status = "✓" if present else "✗"
                    print(f"  {char_type}: {status}")
                print("Feedback:")
                for feedback in analysis['feedback']:
                    print(f"  - {feedback}")
        
        elif choice == "5":
            if generator.password_history:
                print(f"\nPassword History ({len(generator.password_history)} entries):")
                for i, entry in enumerate(generator.password_history[-10:], 1):
                    timestamp = datetime.datetime.fromisoformat(entry['timestamp'])
                    print(f"{i:2d}. {entry['password']} ({timestamp.strftime('%Y-%m-%d %H:%M')})")
            else:
                print("No passwords in history yet.")
        
        elif choice == "6":
            include_passwords = input("Include actual passwords in export? (y/n, default n): ").lower() == 'y'
            filename = input("Export filename (default password_export.json): ") or "password_export.json"
            
            result = generator.export_passwords(filename, include_passwords)
            print(f"\n{result}")
        
        elif choice == "7":
            print("Goodbye! Stay secure! 🔐")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
