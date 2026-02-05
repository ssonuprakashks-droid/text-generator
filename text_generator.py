import random
import re

# Simple Markov chain text generator (no dependencies needed)
class SimpleTextGenerator:
    def __init__(self):
        # Sample training data - a collection of sentences
        self.training_text = """
        The quick brown fox jumps over the lazy dog. A journey of a thousand miles begins with a single step.
        In the beginning there was nothing. Slowly the universe formed. Stars were born and died.
        Technology shapes our world. Artificial intelligence is becoming more important every day.
        The sun rises in the east and sets in the west. Night brings darkness and stars shine bright.
        Learning new skills takes time and dedication. Practice makes perfect in all endeavors.
        Coffee is a beloved beverage around the world. Tea offers a peaceful moment of calm.
        Books provide knowledge and adventure for readers. Stories transport us to different worlds.
        Music brings joy to our hearts and souls. Dance expresses emotion through movement.
        Nature is beautiful and deserves protection. Forests and oceans sustain all life on Earth.
        """
        self.tokens = self._tokenize()
        self.word_chains = self._build_chains()
    
    def _tokenize(self):
        # Simple tokenization by splitting on spaces and punctuation
        words = re.findall(r'\b\w+\b', self.training_text.lower())
        return words
    
    def _build_chains(self):
        # Build word chains for Markov generation
        chains = {}
        for i in range(len(self.tokens) - 1):
            word = self.tokens[i]
            next_word = self.tokens[i + 1]
            if word not in chains:
                chains[word] = []
            chains[word].append(next_word)
        return chains
    
    def generate_text(self, prompt, max_length=100):
        # Generate text starting from the prompt
        prompt_lower = prompt.lower().strip()
        words = prompt_lower.split()
        
        # Start with the last word of the prompt
        current_word = words[-1] if words else random.choice(list(self.word_chains.keys()))
        
        # Remove punctuation from current_word if present
        current_word = re.sub(r'[^\w]', '', current_word)
        
        generated = words.copy()
        
        # Generate words using the chain
        for _ in range(max_length - len(words)):
            if current_word in self.word_chains:
                next_word = random.choice(self.word_chains[current_word])
                generated.append(next_word)
                current_word = next_word
            else:
                # Pick a random word if current word not in chain
                current_word = random.choice(list(self.word_chains.keys()))
                generated.append(current_word)
        
        return ' '.join(generated[:max_length])

if __name__ == "__main__":
    print("Simple Text Generator (Markov Chain)")
    print("-" * 40)
    user_prompt = input("Enter your prompt: ")
    
    generator = SimpleTextGenerator()
    result = generator.generate_text(user_prompt)
    
    print("\nGenerated Text:\n")
    print(result)
