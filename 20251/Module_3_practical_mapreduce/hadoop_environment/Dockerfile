# ---------- Hadoop + YARN + Python + mrjob (Single Node) ----------
FROM ubuntu:22.04

# Avoid interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# ---- Install system dependencies ----
RUN apt-get update && \
    apt-get install -y \
        openjdk-8-jdk \
        wget \
        openssh-client \
        openssh-server \
        python3 \
        python3-pip \
        net-tools \
        sudo && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- Install Hadoop ----
ENV HADOOP_VERSION=3.4.1
RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz -C /opt && \
    mv /opt/hadoop-${HADOOP_VERSION} /opt/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# ---- Install Python packages ----
RUN pip3 install mrjob

# ---- Environment variables ----
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_SECURE_DN_USER=""

# ---- Configure Hadoop to run as root ----
RUN echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> $HADOOP_CONF_DIR/hadoop-env.sh && \
    echo 'export HDFS_NAMENODE_USER=root' >> $HADOOP_CONF_DIR/hadoop-env.sh && \
    echo 'export HDFS_DATANODE_USER=root' >> $HADOOP_CONF_DIR/hadoop-env.sh && \
    echo 'export HDFS_SECONDARYNAMENODE_USER=root' >> $HADOOP_CONF_DIR/hadoop-env.sh && \
    echo 'export YARN_RESOURCEMANAGER_USER=root' >> $HADOOP_CONF_DIR/hadoop-env.sh && \
    echo 'export YARN_NODEMANAGER_USER=root' >> $HADOOP_CONF_DIR/hadoop-env.sh

# ---- Minimal single-node Hadoop configs ----
RUN echo '<configuration>\n\
  <property><name>fs.defaultFS</name><value>hdfs://localhost:9000</value></property>\n\
</configuration>' > $HADOOP_CONF_DIR/core-site.xml && \
    echo '<configuration>\n\
  <property><name>dfs.replication</name><value>1</value></property>\n\
  <property><name>dfs.namenode.name.dir</name><value>file:/opt/hadoop/dfs/name</value></property>\n\
  <property><name>dfs.datanode.data.dir</name><value>file:/opt/hadoop/dfs/data</value></property>\n\
</configuration>' > $HADOOP_CONF_DIR/hdfs-site.xml && \
    echo '<configuration>\n\
  <property><name>yarn.nodemanager.aux-services</name><value>mapreduce_shuffle</value></property>\n\
</configuration>' > $HADOOP_CONF_DIR/yarn-site.xml && \
    echo '<configuration>\n\
  <property><name>mapreduce.framework.name</name><value>yarn</value></property>\n\
  <property><name>yarn.app.mapreduce.am.env</name><value>HADOOP_MAPRED_HOME=/opt/hadoop</value></property>\n\
  <property><name>mapreduce.map.env</name><value>HADOOP_MAPRED_HOME=/opt/hadoop</value></property>\n\
  <property><name>mapreduce.reduce.env</name><value>HADOOP_MAPRED_HOME=/opt/hadoop</value></property>\n\
</configuration>' > $HADOOP_CONF_DIR/mapred-site.xml

# ---- Configure passwordless SSH for root ----
RUN mkdir -p /var/run/sshd && \
    ssh-keygen -t rsa -P "" -f /root/.ssh/id_rsa && \
    cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys && \
    chmod 600 /root/.ssh/authorized_keys && \
    chmod 700 /root/.ssh

# ---- Add startup script ----
RUN echo '#!/bin/bash\n\
service ssh start\n\
if [ ! -d /opt/hadoop/dfs/name/current ]; then\n\
  echo "Formatting HDFS..."\n\
  hdfs namenode -format\n\
fi\n\
echo "Starting HDFS and YARN..."\n\
start-dfs.sh\n\
start-yarn.sh\n\
echo "HDFS UI: http://localhost:9870"\n\
echo "YARN UI: http://localhost:8088"\n\
tail -f /dev/null' > /start-hadoop.sh && chmod +x /start-hadoop.sh

# ---- Networking ----
EXPOSE 9870 8088 22

# ---- Working directory ----
WORKDIR /opt/hadoop

# ---- Default command ----
CMD ["/start-hadoop.sh"]
