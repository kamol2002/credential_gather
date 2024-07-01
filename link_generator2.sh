#!/bin/bash


# Read usernames and passwords from CSV files
usernames=($(cat usernames.csv))
passwords=($(cat passwords.csv))

# Define array of hostnames
HOSTS=("linkedin.com" "gmail.com" "hackerone.com" "tryhackme.com")

# Check if the number of usernames matches passwords
if [ ${#usernames[@]} -ne ${#passwords[@]} ]; then
    echo "Error: The number of usernames and passwords must match."
    exit 1
fi

# Create the output file
output_file="urls.csv"
> "$output_file"

# Generate URLs
for ((i=0; i<${#usernames[@]}; i++)); do
    # Pick a random hostname
    random_host=${HOSTS[RANDOM % ${#HOSTS[@]}]}
    
    # Create the URL
    url="https://${usernames[i]}:${passwords[i]}@$random_host/"
    
    # Write to the output file
    echo "$url" >> "$output_file"
done

echo "URLs have been written to $output_file."


