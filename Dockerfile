# FROM golang:1.13
# WORKDIR /go/src/github.com/alexellis/href-counter/
# COPY vendor vendor
# COPY app.go .
# RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffic cgo -o app .
# FROM alpine:3.10
# RUN apk --no-cache add ca-certificates
# WORKDIR /root/
# COPY --from=0 /go/src/github.com/alexellis/href-counter/   .
# CMD {"./app"}

# FROM alpine
# ENV NR_SLEEPER="5"
# RUN apk add vim
# CMD sleep ${NR_SLEEPER}

FROM ubuntu:18.04
RUN apk add vim
CMD sleep 1000