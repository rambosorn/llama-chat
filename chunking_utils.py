def recursive_character_text_splitter(text, chunk_size, chunk_overlap):
    """
    Splits text into chunks of a specified size with overlap.
    Tries to split on paragraphs (\n\n), then newlines (\n), then spaces.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    
    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = start + chunk_size
        
        if end >= text_len:
            chunks.append(text[start:])
            break
            
        # Try to find a good breaking point (look back from 'end')
        # Priority: Double Newline -> Newline -> Space
        
        # Look for double newline (paragraph break)
        split_point = text.rfind('\n\n', start, end)
        
        if split_point == -1:
            # Look for single newline
            split_point = text.rfind('\n', start, end)
            
        if split_point == -1:
            # Look for space
            split_point = text.rfind(' ', start, end)
            
        if split_point == -1:
            # Force split at chunk_size if no separator found
            split_point = end
        
        # If we found a separator, we want to include it or split after it?
        # Usually split after. 'rfind' gives index of start of substring.
        # For simplicity, let's just use the index found.
        
        # Determine actual end of this chunk
        chunk_end = split_point if split_point != end else end
        
        # Add chunk
        # Strip to clean up edge whitespace
        chunks.append(text[start:chunk_end].strip())
        
        # Move start forward, subtracting overlap
        # Ensure we always move forward at least 1 character to avoid infinite loops
        next_start = chunk_end - chunk_overlap
        if next_start <= start:
             next_start = start + 1 # Force progress
             
        start = next_start

    return [c for c in chunks if c] # Remove empty chunks

def chunk_structured_data(df):
    """
    Converts a pandas DataFrame into a list of string chunks,
    where each chunk represents a single row.
    
    Format:
    "Product: Widget A, Category: Tools, Sales: 500, Region: North"
    """
    chunks = []
    
    # Iterate over rows
    for index, row in df.iterrows():
        # Create a string representation of the row
        # Filter out null values to keep chunks clean
        row_str = ", ".join([f"{col}: {val}" for col, val in row.items() if str(val) != 'nan' and str(val) != 'None'])
        chunks.append(row_str)
        
    return chunks
