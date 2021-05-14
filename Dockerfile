FROM ubuntu:18.04
WORKDIR /home
RUN apt-get update && apt-get install -y \
    maven \
    git \
    openjdk-11-jdk \
RUN adduser newuser
# RUN -fsSL https://get.docker.com -o get-docker.sh
# RUN sh get-docker.sh


# ARG JAR_FILE="target/*.jar"

# COPY ${JAR_FILE} /

# ENV 

# USER 10000

# CMD java -jar /app.jar

# CMD ["java", "-jar", "panda-0.0.1.jar"]

# ENTRYPOINT ["java", "-jar", "/test.jar"]