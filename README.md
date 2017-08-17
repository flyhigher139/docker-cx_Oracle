
# How to use this repo?

This is an example to connect to oracle with docker in python.

You can use this repo to test your oracle connections:

1\. Get this docker cx_Oracle image

You can pull this image from dockerhub:

```
$ docker pull gevin/docker_cx_oracle
```

alternatively, you can build your own image:

```bash
$ docker build -t docker_cx_oracle .
```

2\. Start a container

```bash
$ (sudo) docker run --rm -it gevin/docker_cx_oracle bash
```

3\. Set oracle connection information with environment variables

```bash
$ export hostname=10.215.1.163
$ export port=1521
$ export instance=my_instance
$ export username=gevin
$ export password=password
```

4\. Run this command to check whether succeed to connect oracle database or not

```bash
python connection_test.py
```

5\. Exit this container

# What's more

[Oracle Instant Client license](http://www.oracle.com/technetwork/licenses/distribution-license-152002.html)

[Using Python With Oracle Database 11g](http://www.oracle.com/technetwork/articles/dsl/python-091105.html)
