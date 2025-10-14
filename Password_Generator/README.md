# Advanced Password Generator 🔐

A comprehensive and secure password generator that creates strong, customizable passwords with advanced security features and analysis capabilities.

## Features

- 🔒 **Secure Generation**: Uses cryptographically secure random number generation
- 🎯 **Customizable Options**: Control length, character sets, and requirements
- 📊 **Strength Analysis**: Detailed password strength evaluation and feedback
- 🧠 **Passphrase Generation**: Create memorable passphrases using common words
- 📈 **Bulk Generation**: Generate multiple passwords at once
- 📝 **Password History**: Track generated passwords with timestamps
- 💾 **Export Functionality**: Save password history to files
- 🔍 **Pattern Detection**: Identifies common weak patterns
- 📊 **Entropy Calculation**: Measures password randomness and security

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd Password_Generator

# No external dependencies required - uses only Python standard library
python password_generator.py
```

## Usage

### Interactive Mode
```bash
python password_generator.py
```

### Programmatic Usage
```python
from password_generator import PasswordGenerator

# Create generator instance
generator = PasswordGenerator()

# Generate a secure password
password = generator.generate_password(
    length=16,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_symbols=True,
    min_uppercase=2,
    min_lowercase=2,
    min_digits=2,
    min_symbols=2
)

# Analyze password strength
analysis = generator.analyze_password_strength(password)
print(f"Password: {password}")
print(f"Strength: {analysis['strength']}")
print(f"Score: {analysis['score']}/8")
```

## Password Generation Options

### Single Password
- **Length**: 8-128 characters (default: 12)
- **Character Sets**: Uppercase, lowercase, digits, symbols
- **Minimum Requirements**: Set minimum counts for each character type
- **Exclusions**: Remove similar/ambiguous characters

### Passphrase Generation
- **Word Count**: 3-10 words (default: 4)
- **Separators**: Custom separators between words
- **Capitalization**: Optional word capitalization
- **Numbers & Symbols**: Optional random additions

### Bulk Generation
- Generate multiple passwords with same settings
- Useful for creating password lists
- Maintains individual password strength

## Password Strength Analysis

The generator provides comprehensive strength analysis:

- **Length Analysis**: Evaluates password length
- **Character Variety**: Checks for multiple character types
- **Pattern Detection**: Identifies common weak patterns
- **Entropy Calculation**: Measures randomness and security
- **Strength Levels**: Weak, Medium, Strong, Very Strong

### Strength Scoring
- **0-1**: Weak (easily cracked)
- **2-3**: Medium (moderate security)
- **4-5**: Strong (good security)
- **6-8**: Very Strong (excellent security)

## Security Features

- **Cryptographically Secure**: Uses `secrets` module for true randomness
- **No Weak Patterns**: Avoids common patterns like "123", "abc", "qwerty"
- **Character Exclusions**: Option to exclude similar/ambiguous characters
- **Minimum Requirements**: Ensures password meets complexity requirements
- **Entropy Analysis**: Calculates and reports password entropy

## Examples

### Strong Password Generation
```
Generated Password: K9#mP2$vL8@nQ4!
Strength: VERY_STRONG
Score: 8/8
Entropy: 78.45
```

### Passphrase Generation
```
Generated Passphrase: Dragon-Sunset-Mountain-River-42!
Strength: STRONG
Score: 6/8
```

### Bulk Generation
```
Generated 5 passwords:
 1. mK7#nP9$vL2@qR5!
 2. X3&bN8*vM4@tS6#
 3. Q9$cF2#wH5@yU7!
 4. Z6&dG8*vJ3@kI4#
 5. L1$eH9#xK7@mN2!
```

## File Structure

```
Password_Generator/
├── password_generator.py    # Main generator class and functions
├── README.md               # This documentation
└── requirements.txt        # Dependencies (none required)
```

## Contributing

Contributions are welcome! Areas for improvement:
- Additional character sets
- More sophisticated pattern detection
- Integration with password managers
- GUI interface
- Additional export formats
- Password policy validation

## Security Notes

- This tool generates passwords locally - no data is sent to external servers
- Password history is stored locally and can be exported
- Use strong, unique passwords for all accounts
- Consider using a password manager for long-term storage
- Regularly update passwords for critical accounts

## License

This project is open source and available under the MIT License.

---

**Remember**: The best password is one that's both strong and memorable. Use this tool responsibly and never share your passwords!
