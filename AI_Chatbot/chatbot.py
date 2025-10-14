#!/usr/bin/env python3
"""
AI Chatbot - Intelligent Conversational Assistant
=================================================

A simple yet powerful AI chatbot that can:
- Answer questions intelligently
- Provide weather information
- Calculate mathematical expressions
- Tell jokes and stories
- Help with programming concepts
- Remember conversation context

Author: AI Assistant
Language: Python 3
Dependencies: requests, datetime, random, json
"""

import json
import random
import datetime
import requests
import re
import math

class AIChatbot:
    def __init__(self):
        self.name = "AI Assistant"
        self.conversation_history = []
        self.user_name = ""
        
        # Knowledge base
        self.responses = {
            "greeting": [
                "Hello! I'm your AI assistant. How can I help you today?",
                "Hi there! What would you like to know?",
                "Greetings! I'm here to assist you with anything you need.",
                "Hello! Ready to chat and help you out!"
            ],
            "farewell": [
                "Goodbye! It was nice talking to you!",
                "See you later! Feel free to come back anytime.",
                "Take care! Have a great day!",
                "Farewell! Remember, I'm always here to help."
            ],
            "jokes": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "What do you call a fake noodle? An impasta!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a bear with no teeth? A gummy bear!"
            ],
            "programming_tips": [
                "Always write clean, readable code with meaningful variable names.",
                "Comment your code - your future self will thank you!",
                "Test your code thoroughly before deploying.",
                "Use version control (Git) for all your projects.",
                "Learn one programming language deeply before moving to others."
            ]
        }
    
    def get_weather(self, city="Jakarta"):
        """Get weather information for a city"""
        try:
            # Using a free weather API (OpenWeatherMap)
            api_key = "demo_key"  # Replace with actual API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            
            # For demo purposes, return mock data
            mock_weather = {
                "Jakarta": "Sunny, 32°C",
                "Bandung": "Cloudy, 28°C", 
                "Surabaya": "Rainy, 26°C",
                "Yogyakarta": "Partly cloudy, 30°C"
            }
            
            return f"The weather in {city} is: {mock_weather.get(city, 'Weather data not available')}"
        except:
            return "Sorry, I couldn't fetch weather data right now."
    
    def calculate_math(self, expression):
        """Safely evaluate mathematical expressions"""
        try:
            # Remove dangerous functions and only allow safe math operations
            safe_dict = {
                "__builtins__": {},
                "abs": abs, "round": round, "min": min, "max": max,
                "sum": sum, "pow": pow, "sqrt": math.sqrt,
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "log": math.log, "pi": math.pi, "e": math.e
            }
            
            # Clean the expression
            expression = re.sub(r'[^0-9+\-*/().\s]', '', expression)
            result = eval(expression, safe_dict)
            return f"The result is: {result}"
        except:
            return "Sorry, I couldn't calculate that. Please check your math expression."
    
    def tell_story(self):
        """Tell a random short story"""
        stories = [
            "Once upon a time, there was a little robot who dreamed of becoming a painter. Every day, it would collect colorful data and create beautiful digital art. The robot's art became so popular that it inspired humans to see the world in new ways.",
            "In a distant galaxy, there lived a wise alien who could speak every programming language in the universe. One day, it met a curious human programmer, and together they created the most efficient algorithm ever known.",
            "There was a magical computer that could solve any problem, but it had one condition: you had to ask the right question. Many tried, but only those who understood the problem deeply could unlock its power."
        ]
        return random.choice(stories)
    
    def process_message(self, user_input):
        """Process user input and generate appropriate response"""
        user_input = user_input.lower().strip()
        
        # Store conversation
        self.conversation_history.append(f"User: {user_input}")
        
        # Greeting detection
        if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
            if not self.user_name:
                self.user_name = input("What's your name? ")
                return f"Nice to meet you, {self.user_name}! " + random.choice(self.responses["greeting"])
            return random.choice(self.responses["greeting"])
        
        # Farewell detection
        if any(word in user_input for word in ["bye", "goodbye", "see you", "farewell"]):
            return random.choice(self.responses["farewell"])
        
        # Weather request
        if "weather" in user_input:
            city = "Jakarta"  # Default city
            words = user_input.split()
            for i, word in enumerate(words):
                if word == "in" and i + 1 < len(words):
                    city = words[i + 1].capitalize()
            return self.get_weather(city)
        
        # Math calculation
        if any(op in user_input for op in ["+", "-", "*", "/", "calculate", "math", "="]):
            # Extract mathematical expression
            math_pattern = r'[\d+\-*/().\s]+'
            match = re.search(math_pattern, user_input)
            if match:
                expression = match.group().strip()
                return self.calculate_math(expression)
        
        # Joke request
        if any(word in user_input for word in ["joke", "funny", "laugh"]):
            return random.choice(self.responses["jokes"])
        
        # Story request
        if any(word in user_input for word in ["story", "tell me", "narrative"]):
            return self.tell_story()
        
        # Programming help
        if any(word in user_input for word in ["programming", "code", "coding", "developer", "programmer"]):
            return random.choice(self.responses["programming_tips"])
        
        # Time and date
        if any(word in user_input for word in ["time", "date", "what time", "what date"]):
            now = datetime.datetime.now()
            return f"Current time: {now.strftime('%H:%M:%S')}, Date: {now.strftime('%Y-%m-%d')}"
        
        # Default responses
        default_responses = [
            "That's interesting! Can you tell me more about that?",
            "I'm not sure I understand. Could you rephrase that?",
            "That's a great question! Let me think about it...",
            "I'm learning new things every day. What else would you like to know?",
            "Fascinating! I'd love to hear more about your thoughts on this."
        ]
        
        return random.choice(default_responses)
    
    def chat(self):
        """Main chat loop"""
        print(f"🤖 {self.name} is online!")
        print("=" * 50)
        print("Type 'quit' or 'exit' to end the conversation")
        print("Try asking about weather, math, jokes, stories, or programming!")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"\n{self.name}: {random.choice(self.responses['farewell'])}")
                    break
                
                if not user_input:
                    continue
                
                response = self.process_message(user_input)
                print(f"\n{self.name}: {response}")
                
                # Store bot response
                self.conversation_history.append(f"Bot: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"\n{self.name}: Oops! Something went wrong: {e}")
    
    def save_conversation(self, filename="conversation_history.json"):
        """Save conversation history to file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.conversation_history, f, indent=2)
            print(f"Conversation saved to {filename}")
        except Exception as e:
            print(f"Could not save conversation: {e}")

def main():
    """Main function to run the chatbot"""
    print("🚀 Starting AI Chatbot...")
    
    # Create and run chatbot
    bot = AIChatbot()
    bot.chat()
    
    # Ask if user wants to save conversation
    try:
        save = input("\nWould you like to save this conversation? (y/n): ").lower()
        if save == 'y':
            bot.save_conversation()
    except:
        pass
    
    print("\n👋 Thanks for using AI Chatbot!")

if __name__ == "__main__":
    main()
