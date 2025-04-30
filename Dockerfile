# Use a lightweight base image
FROM ubuntu:latest

# Avoid interactive prompt
ENV PATH="${PATH}:/usr/games"
# Install dependencies
RUN apt-get update && apt-get install && apt install \
    fortune \
    cowsay \
    netcat-openbsd \
    git -y
    

# Set working director
WORKDIR /app

# Clone your GitHub repository (replace with your actual repo)
#RUN git clone https://github.com/nyrahul/wisecow.git .

#RUN chmod +x wisecow.sh
# Make the script executable
# Copy the local wisecow.sh script into the image
COPY wisecow.sh /app/wisecow.sh

# Make the script executable
RUN chmod +x /app/wisecow.sh

# Expose the default port
EXPOSE 4499

# Run the server
CMD ["./wisecow.sh"]
