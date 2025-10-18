import requests
import os

def search_web(query, max_results=3):
    api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
    search_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
    
    # If API keys are not set, return enhanced fallback sources
    if not api_key or api_key == 'your_google_search_api_key_here':
        print("⚠️  Google Search API key not configured, using enhanced fallback sources")
        return get_enhanced_fallback_sources(query)
    
    if not search_engine_id or search_engine_id == 'your_search_engine_id_here':
        print("⚠️  Google Search Engine ID not configured, using enhanced fallback sources")
        return get_enhanced_fallback_sources(query)
    
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': query,
        'num': max_results
    }
    
    try:
        print(f"🔍 Searching Google for: '{query}'")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Search API returned status {response.status_code}")
            return get_enhanced_fallback_sources(query)
            
        results = response.json()
        
        search_results = []
        if 'items' in results:
            for item in results['items'][:max_results]:
                search_results.append({
                    'title': item.get('title', 'No title'),
                    'link': item.get('link', '#'),
                    'snippet': item.get('snippet', 'No description available')
                })
            print(f"✅ Found {len(search_results)} results")
        else:
            print(f"⚠️  No search results found in API response")
            search_results = get_enhanced_fallback_sources(query)
            
        return search_results
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Search API error: {e}")
        return get_enhanced_fallback_sources(query)
    except Exception as e:
        print(f"❌ Unexpected search error: {e}")
        return get_enhanced_fallback_sources(query)

def get_enhanced_fallback_sources(query):
    """Return comprehensive fallback sources when search API fails"""
    
    # Base internet slang sources
    base_sources = [
        {
            'title': 'Wikipedia - Internet Slang',
            'link': 'https://en.wikipedia.org/wiki/Internet_slang',
            'snippet': 'Comprehensive overview of internet slang, acronyms, and their historical development.'
        },
        {
            'title': 'Urban Dictionary',
            'link': 'https://www.urbandictionary.com/',
            'snippet': 'Crowdsourced online dictionary of slang words, phrases, and cultural references.'
        },
        {
            'title': 'NetLingo Internet Dictionary',
            'link': 'https://www.netlingo.com/',
            'snippet': 'Extensive dictionary of internet slang, acronyms, and text messaging shorthand.'
        }
    ]
    
    # Specific sources for common terms
    specific_sources = {
        'brb': {
            'title': 'BRB - What does BRB mean?',
            'link': 'https://www.cyberdefinitions.com/definitions/BRB.html',
            'snippet': 'BRB stands for "Be Right Back". Used in text and chat to indicate temporary absence.'
        },
        'afk': {
            'title': 'AFK - Away From Keyboard',
            'link': 'https://www.cyberdefinitions.com/definitions/AFK.html',
            'snippet': 'AFK means "Away From Keyboard". Indicates temporary unavailability in online contexts.'
        },
        'lol': {
            'title': 'LOL - Laughing Out Loud',
            'link': 'https://www.cyberdefinitions.com/definitions/LOL.html',
            'snippet': 'LOL stands for "Laughing Out Loud". One of the most common internet acronyms.'
        },
        'omg': {
            'title': 'OMG - Oh My God',
            'link': 'https://www.cyberdefinitions.com/definitions/OMG.html',
            'snippet': 'OMG means "Oh My God". Expresses surprise, excitement, or shock.'
        },
        'ttyl': {
            'title': 'TTYL - Talk To You Later',
            'link': 'https://www.cyberdefinitions.com/definitions/TTYL.html',
            'snippet': 'TTYL stands for "Talk To You Later". Used to end conversations temporarily.'
        },
        'imo': {
            'title': 'IMO - In My Opinion',
            'link': 'https://www.cyberdefinitions.com/definitions/IMO.html',
            'snippet': 'IMO means "In My Opinion". Prefaces subjective statements in online discussions.'
        },
        'smh': {
            'title': 'SMH - Shaking My Head',
            'link': 'https://www.cyberdefinitions.com/definitions/SMH.html',
            'snippet': 'SMH means "Shaking My Head". Expresses disappointment or disbelief.'
        },
        'g2g': {
            'title': 'G2G - Got To Go',
            'link': 'https://www.cyberdefinitions.com/definitions/G2G.html',
            'snippet': 'G2G means "Got To Go". Indicates urgent departure from conversation.'
        }
    }
    
    # Historical/archaeological sources
    historical_sources = [
        {
            'title': 'Textual Criticism - Wikipedia',
            'link': 'https://en.wikipedia.org/wiki/Textual_criticism',
            'snippet': 'Study of textual reconstruction and analysis of historical documents and manuscripts.'
        },
        {
            'title': 'Papyrology - Ancient Document Study',
            'link': 'https://en.wikipedia.org/wiki/Papyrology',
            'snippet': 'Academic discipline concerned with the study of ancient texts on papyrus and other materials.'
        }
    ]
    
    # MySpace and historical platform sources
    myspace_sources = [
        {
            'title': 'MySpace Top 8 - Wikipedia',
            'link': 'https://en.wikipedia.org/wiki/Myspace#Features',
            'snippet': 'Explanation of MySpace Top Friends feature and its social impact in the 2000s.'
        },
        {
            'title': 'Internet History - MySpace',
            'link': 'https://en.wikipedia.org/wiki/Myspace',
            'snippet': 'Historical overview of MySpace and its cultural significance in early social media.'
        }
    ]
    
    # Start with base sources
    results = base_sources.copy()
    
    # Add specific sources based on query content
    query_lower = query.lower()
    for term, source in specific_sources.items():
        if term in query_lower:
            results.append(source)
    
    # Add historical sources if relevant
    if any(term in query_lower for term in ['ancient', 'scroll', 'manuscript', 'historical', 'artifact', 'treasure']):
        results.extend(historical_sources)
    
    # Add MySpace sources if relevant
    if 'top 8' in query_lower or 'myspace' in query_lower:
        results.extend(myspace_sources)
    
    # Remove duplicates and ensure we don't return too many sources
    unique_results = []
    seen_titles = set()
    for result in results:
        if result['title'] not in seen_titles:
            seen_titles.add(result['title'])
            unique_results.append(result)
    
    return unique_results[:4]  # Return max 4 sources