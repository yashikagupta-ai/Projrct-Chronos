import os
import argparse
from dotenv import load_dotenv
from utils.gemini_client import reconstruct_text
from utils.search_client import search_web
from utils.report_generator import generate_report

def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Project Chronos: AI Archeologist')
    parser.add_argument('text', type=str, help='Fragmented text to reconstruct')
    args = parser.parse_args()
    
    print("🔍 Project Chronos - AI Archeologist")
    print("Processing your fragmented text...")
    
    # Step 1: Reconstruct text using Gemini
    reconstructed_text = reconstruct_text(args.text)
    
    # Step 2: Search for contextual information
    search_results = search_web(reconstructed_text)
    
    # Step 3: Generate final report
    report = generate_report(args.text, reconstructed_text, search_results)
    
    print("\n" + "="*50)
    print(report)
    print("="*50)

if __name__ == "__main__":
    main()