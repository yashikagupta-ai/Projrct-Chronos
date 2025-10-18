#!/usr/bin/env python3
import os
import argparse
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    print("🔍 Project Chronos - AI Archeologist")
    print("=" * 50)
    
    try:
        from utils.gemini_client import reconstruct_text
        from utils.search_client import search_web
        from utils.report_generator import generate_report
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please check your file structure.")
        return
    
    parser = argparse.ArgumentParser(description='Project Chronos: AI Archeologist')
    parser.add_argument('text', type=str, help='Fragmented text to reconstruct')
    args = parser.parse_args()
    
    if not args.text.strip():
        print("❌ Please provide text to reconstruct")
        return
    
    print(f"📜 Original fragment: '{args.text}'")
    print("\n" + "=" * 50)
    
    # Step 1: Reconstruct text
    print("🔄 Step 1: Reconstructing text using AI...")
    reconstructed_text = reconstruct_text(args.text)
    
    if reconstructed_text.startswith("Error:"):
        print(f"❌ Reconstruction failed: {reconstructed_text}")
        return
    
    print(f"✅ Reconstructed: {reconstructed_text}")
    print("\n" + "=" * 50)
    
    # Step 2: Search for context - use smarter search queries based on text type
    print("🔍 Step 2: Searching for contextual information...")
    
    # Analyze text type to create better search queries
    text_lower = args.text.lower()

    if any(term in text_lower for term in ['brb', 'afk', 'lol', 'omg', 'ttyl', 'imo', 'wtf']):
        # Internet slang text
        search_queries = [
            f"\"{args.text}\" internet slang meaning",
            "common internet acronyms abbreviations",
            "online chat slang dictionary"
        ]
    elif any(term in text_lower for term in ['ancient', 'scroll', 'manuscript', 'historical', 'treasure']):
        # Historical/archaeological text
        search_queries = [
            f"\"{args.text}\" historical documents",
            "ancient manuscript reconstruction",
            "archaeological text analysis"
        ]
    else:
        # General text
        search_queries = [
            f"\"{args.text}\"",
            "text reconstruction techniques",
            "linguistic analysis"
        ]

    all_search_results = []
    for query in search_queries:
        results = search_web(query, max_results=2)
        all_search_results.extend(results)
        if len(all_search_results) >= 4:  # Don't get too many
            break
    
    # Remove duplicates based on URL
    unique_results = []
    seen_urls = set()
    for result in all_search_results:
        if result['link'] not in seen_urls:
            seen_urls.add(result['link'])
            unique_results.append(result)
    
    print(f"✅ Found {len(unique_results)} contextual sources")
    print("\n" + "=" * 50)
    
    # Step 3: Generate report
    print("📊 Step 3: Generating comprehensive report...")
    report = generate_report(args.text, reconstructed_text, unique_results)
    
    print("\n" + "=" * 60)
    print(report)
    print("=" * 60)

if __name__ == "__main__":
    main()