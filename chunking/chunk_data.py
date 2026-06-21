from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read website data
with open("website_data.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Generate chunks
chunks = splitter.split_text(text)

# Print total chunks
print("Total Chunks:", len(chunks))

# Save chunks
with open("chunks.txt", "w", encoding="utf-8") as f:

    for i, chunk in enumerate(chunks):

        f.write(f"\n\n===== CHUNK {i+1} =====\n\n")
        f.write(chunk)

print("Chunks saved successfully!")