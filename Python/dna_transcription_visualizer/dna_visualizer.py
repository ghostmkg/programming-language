import time
import random
import colorama
from colorama import Fore, Back, Style
import os

# Initialize colorama for Windows compatibility
colorama.init(autoreset=True)

class DNATranscriptionVisualizer:
    def __init__(self):
        self.dna_colors = {
            'A': Fore.GREEN,
            'T': Fore.RED,
            'G': Fore.YELLOW,
            'C': Fore.BLUE
        }
        self.rna_colors = {
            'A': Fore.GREEN,
            'U': Fore.MAGENTA,  # U replaces T in RNA
            'G': Fore.YELLOW,
            'C': Fore.BLUE
        }
        self.complementary_bases = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }
        self.rna_bases = {
            'A': 'U',  # In RNA, T is replaced by U
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def validate_dna_sequence(self, sequence):
        """Validate if the input sequence contains only valid DNA bases."""
        valid_bases = set('ATGC')
        return all(base in valid_bases for base in sequence.upper())

    def generate_random_dna(self, length=20):
        """Generate a random DNA sequence of specified length."""
        return ''.join(random.choice('ATGC') for _ in range(length))

    def display_base_with_color(self, base, is_rna=False):
        """Display a base with its corresponding color."""
        colors = self.rna_colors if is_rna else self.dna_colors
        return f"{colors[base]}{base}{Style.RESET_ALL}"

    def animate_transcription(self, dna_sequence):
        """Animate the DNA to RNA transcription process."""
        self.clear_screen()
        print("\n=== DNA to RNA Transcription Visualizer ===\n")
        
        # Display original DNA sequence
        print("Original DNA Sequence:")
        print(''.join(self.display_base_with_color(base) for base in dna_sequence))
        print("=" * len(dna_sequence))
        
        # Animate transcription process
        rna_sequence = ""
        for base in dna_sequence:
            time.sleep(0.5)  # Add delay for animation
            rna_base = self.rna_bases[base]
            rna_sequence += rna_base
            
            # Clear and redisplay
            self.clear_screen()
            print("\n=== DNA to RNA Transcription Visualizer ===\n")
            print("Original DNA Sequence:")
            print(''.join(self.display_base_with_color(base) for base in dna_sequence))
            print("=" * len(dna_sequence))
            print("\nRNA Sequence being transcribed:")
            print(''.join(self.display_base_with_color(b, True) for b in rna_sequence) + 
                  " " * (len(dna_sequence) - len(rna_sequence)))
            
            # Show explanation
            print(f"\nTranscribing: DNA {base} → RNA {rna_base}")
            
        print("\nTranscription Complete!")
        return rna_sequence

    def interactive_menu(self):
        """Display interactive menu and handle user input."""
        while True:
            self.clear_screen()
            print("\n=== DNA Transcription Visualizer ===")
            print("1. Enter custom DNA sequence")
            print("2. Generate random DNA sequence")
            print("3. Learn about DNA transcription")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == '1':
                sequence = input("\nEnter DNA sequence (using A, T, G, C only): ").upper()
                if self.validate_dna_sequence(sequence):
                    self.animate_transcription(sequence)
                    input("\nPress Enter to continue...")
                else:
                    print("\nInvalid DNA sequence! Use only A, T, G, C.")
                    time.sleep(2)
            
            elif choice == '2':
                length = int(input("\nEnter desired sequence length (5-50): "))
                length = max(5, min(50, length))  # Limit length between 5 and 50
                sequence = self.generate_random_dna(length)
                self.animate_transcription(sequence)
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                self.show_educational_content()
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                print("\nThank you for learning about DNA transcription!")
                break

    def show_educational_content(self):
        """Display educational content about DNA transcription."""
        self.clear_screen()
        print(f"""
{Fore.CYAN}=== Understanding DNA Transcription ==={Style.RESET_ALL}

DNA transcription is a fundamental process in molecular biology where DNA is used as a template 
to create RNA. This process is essential for gene expression and protein synthesis.

Key Points:
{Fore.GREEN}1. Base Pairing Rules:{Style.RESET_ALL}
   - DNA to RNA transcription follows specific base pairing rules
   - A (Adenine) pairs with U (Uracil) in RNA (instead of T in DNA)
   - G (Guanine) pairs with C (Cytosine)

{Fore.YELLOW}2. Process:{Style.RESET_ALL}
   - DNA double helix unwinds
   - RNA nucleotides pair with exposed DNA bases
   - RNA strand grows in the 5' to 3' direction

{Fore.MAGENTA}3. Importance:{Style.RESET_ALL}
   - Creates messenger RNA (mRNA)
   - Essential for protein synthesis
   - Key step in gene expression

Color Guide in This Visualizer:
   {Fore.GREEN}Green: Adenine (A)
   {Fore.RED}Red: Thymine (T)
   {Fore.YELLOW}Yellow: Guanine (G)
   {Fore.BLUE}Blue: Cytosine (C)
   {Fore.MAGENTA}Magenta: Uracil (U) in RNA{Style.RESET_ALL}
""")

if __name__ == "__main__":
    visualizer = DNATranscriptionVisualizer()
    visualizer.interactive_menu()