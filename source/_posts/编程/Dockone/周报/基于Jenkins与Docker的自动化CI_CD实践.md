
---
title: '基于Jenkins与Docker的自动化CI_CD实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/37f027ba078b6d65f9a4e0fdde957b11.png'
author: Dockone
comments: false
date: 2021-04-28 08:08:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/37f027ba078b6d65f9a4e0fdde957b11.png'
---

<div>   
<br>高效的CI/CD环境能获得什么呢？<br>
<ol><li>及时发现问题：提早得到集成反馈和修复</li><li>大幅度减少故障率：业务流程化，减少人工出错风险</li><li>加快迭代速度：可以在几分钟内运行几十次、甚至上百次持续集成</li><li>减少时间成本：多项目管理及繁琐的部署工作没有了，不必再花费一定时间去准备</li><li>研发端到端流水线，一键部署，应用弹性伸缩，灰度发布</li></ol><br>
<br>要想做到一个高效的CI/CD流程，需要有能力整合DevOps工具链及多环境适配，并且设计之初以自动化为原则，如一键部署、一键升级。<br>
<h3>发布流程设计</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/37f027ba078b6d65f9a4e0fdde957b11.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/37f027ba078b6d65f9a4e0fdde957b11.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/398af1861c37fc82ba96b26fd0dd5a3e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/398af1861c37fc82ba96b26fd0dd5a3e.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>开发语言：Java</li><li>项目代码版本管理：Git</li><li>代码编译：Maven</li><li>持续集成：Jenkins</li><li>交付：以Docker镜像形式交付，提交至Harbor</li><li>部署：Docker主机创建容器</li></ul><br>
<br>环境规划如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/03ef2ef848bb3cb4eb5875be1386280a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/03ef2ef848bb3cb4eb5875be1386280a.png" class="img-polaroid" title="B1.png" alt="B1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
工作流程：<br>
<ol><li>开发人员提交代码到Git版本仓库；</li><li>Jenkins人工/定时触发项目构建；</li><li>Jenkins拉取代码、代码编译、打包镜像、推送到镜像仓库；</li><li>Jenkins在Docker主机创建容器并发布。</li></ol><br>
<br><h3>部署Git仓库</h3>首先部署一个Git仓库，存储测试的代码，这里选择solo博客程序做测试：<a href="https://github.com/b3log/solo" rel="nofollow" target="_blank">https://github.com/b3log/solo</a>。该步骤在192.168.30.130上执行。<br>
<br>安装Git：<br>
<pre class="prettyprint"># yum install -y git<br>
</pre><br>
创建Git用户并设置密码：<br>
<pre class="prettyprint"># useradd git# passwd git<br>
</pre><br>
创建仓库：<br>
<pre class="prettyprint"># su - git# mkdir solo.git# cd solo.git# git init --bare           #创建裸仓库# vim config                #添加用户，否则commit报错[user]<br>
    name = lzx<br>
    email = lzx@lzx.com<br>
</pre><br>
上传项目到仓库：<br>
<br>拉取代码：<br>
<pre class="prettyprint"># git clone https://github.com/b3log/solo.git<br>
</pre><br>
添加私有仓库地址：<br>
<pre class="prettyprint"># cd solo/# git remote remove origin# git remote add origin git@192.168.30.130:/home/git/solo.git<br>
</pre><br>
提交到私有仓库：<br>
<pre class="prettyprint"># git add .# git commit -m "all"# git push origin master<br>
</pre><br>
<h3>部署Harbor镜像仓库</h3>之前部署过，此处省略，参考这里：<a href="https://blog.csdn.net/miss1181248983/article/details/87856200" rel="nofollow" target="_blank">https://blog.csdn.net/miss1181 ... 56200</a><br>
<h3>安装Docker</h3>需要安装Docker及配置Java环镜。 该步骤在192.168.30.128上执行。<br>
<br>安装依赖包：<br>
<pre class="prettyprint"># yum install -y yum-utils device-mapper-persistent-data lvm2<br>
</pre><br>
添加Docker软件包源：<br>
<pre class="prettyprint"># curl http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker.repo<br>
</pre><br>
安装Docker CE：<br>
<pre class="prettyprint"># yum install -y docker-ce<br>
</pre><br>
启动并开机启动：<br>
<pre class="prettyprint"># systemctl start docker && systemctl enable docker<br>
</pre><br>
安装Java和Maven环境：<br>
<pre class="prettyprint"># tar zxf jdk-8u191-linux-x64.tar.gz && mv jdk1.8.0_191/ /usr/local/jdk# wget http://mirrors.shu.edu.cn/apache/maven/maven-3/3.6.0/binaries/apache-maven-3.6.0-bin.tar.gz# tar zxf apache-maven-3.6.0-bin.tar.gz && mv apache-maven-3.6.0/ /usr/local/maven# vim /etc/profileMAVEN_HOME=/usr/local/maven<br>
JAVA_HOME=/usr/local/jdk<br>
PATH=$PATH:$JAVA_HOME/bin:$MAVEN_HOME/bin<br>
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jarexport JAVA_HOME PATH CLASSPATH# source !$<br>
</pre><br>
授权Docker主机免密登陆Git仓库：<br>
<pre class="prettyprint"># ssh-keygen# ssh-copy-id git@192.168.30.130# ssh git@192.168.30.130            #测试登录<br>
</pre><br>
<h3>安装Jenkins</h3>基于CentOS镜像构建Jenkins镜像，同时将安装JDK、Maven。该步骤在192.168.30.129上执行。<br>
<br>编辑Dockerfile：<br>
<pre class="prettyprint"># vim Dockerfile-java<br>
</pre><br>
<pre class="prettyprint">FROM centos:latest<br>
MAINTAINER lzx  lzx@lzxlinux.com<br>
<br>
RUN yum install -y wget vim curl unzip iproute net-tools && \<br>
yum clean all && \<br>
rm -rf /var/cache/yum/*<br>
<br>
ADD jdk-8u191-linux-x64.tar.gz /usr/local/<br>
RUN mv /usr/local/jdk1.8.0_191/ /usr/local/jdk && \<br>
wget http://mirrors.shu.edu.cn/apache/tomcat/tomcat-8/v8.5.39/bin/apache-tomcat-8.5.39.tar.gz && \<br>
tar zxf apache-tomcat-8.5.39.tar.gz && \<br>
mv apache-tomcat-8.5.39 /usr/local/tomcat && \<br>
wget http://mirrors.shu.edu.cn/apache/maven/maven-3/3.6.0/binaries/apache-maven-3.6.0-bin.tar.gz && \<br>
tar zxf apache-maven-3.6.0-bin.tar.gz && \<br>
mv apache-maven-3.6.0 /usr/local/maven && \<br>
wget http://mirrors.jenkins.io/war-stable/latest/jenkins.war && \<br>
rm -rf /usr/local/tomcat/webapps/* && \<br>
unzip jenkins.war -d /usr/local/tomcat/webapps/ROOT && \<br>
rm -rf jenkins.war jdk-* apache-*<br>
ENV JAVA_HOME /usr/local/jdk<br>
ENV JRE_HOME /usr/local/jdk/jre<br>
ENV CATALINA_HOME /usr/local/tomcat<br>
ENV MAVEN_HOME /usr/local/maven<br>
ENV CLASSPATH $JAVA_HOME/lib:$JRE_HOME/lib:$JRE_HOME/lib/charsets.jar<br>
<br>
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/lib:$MAVEN_HOME/bin<br>
WORKDIR /usr/local/tomcat<br>
EXPOSE 8080<br>
CMD ["catalina.sh","run"]<br>
</pre><br>
Docker构建Jenkins镜像：<br>
<pre class="prettyprint"># docker build -t jenkins-2.164 -f Dockerfile-java .<br>
</pre><br>
启动Jenkins：<br>
<pre class="prettyprint"># docker run -d -p 8080:8080 --name jenkins jenkins-2.164:latest<br>
</pre><br>
启动完打开网页访问<code class="prettyprint">192.168.30.129:8080</code>，安装推荐插件，设置账户密码。<br>
<br>添加凭据：<code class="prettyprint">系统管理</code>  →  <code class="prettyprint">凭据配置</code>  →  <code class="prettyprint">凭据</code>  →  <code class="prettyprint">Jenkins</code>  →  <code class="prettyprint">全局凭据</code>  →  <code class="prettyprint">添加凭据</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/b07391d389199f0d3cfea1fdff9fdb4e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/b07391d389199f0d3cfea1fdff9fdb4e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
新建节点：<code class="prettyprint">系统管理</code>  →  <code class="prettyprint">节点管理</code>  →  <code class="prettyprint">新建节点</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/def3457163af0aba0917c8a884b929f3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/def3457163af0aba0917c8a884b929f3.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
标签请注意不要填错，用于识别哪一个slave执行任务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/5273d2a55ca45c4486ed65b583efefd0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/5273d2a55ca45c4486ed65b583efefd0.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
新建任务：<code class="prettyprint">新建任务</code>  →  <code class="prettyprint">流水线</code>  ，名称任意。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/bade59e1065e40fe6f8b2ef101b3a266.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/bade59e1065e40fe6f8b2ef101b3a266.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/d056ae778e5ca6522658ea91547bb120.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/d056ae778e5ca6522658ea91547bb120.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Jenkinsfile如下：<br>
<pre class="prettyprint">node ("192.168.30.128") &#123;        #指定slave标签#拉取代码stage('Git Checkout') &#123;<br>
checkout([$class: 'GitSCM',branches: [[name: '$Tag']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'git@192.168.30.130:/home/git/solo.git']]])&#125;       #$Tag引用用户交互输入的tag#代码编译stage('Maven Build') &#123;<br>
sh '''<br>
export JAVA_HOME=/usr/local/jdk<br>
/usr/local/maven/bin/mvn clean package -Dmaven.test.skip=true<br>
'''&#125;#项目打包到镜像并推送到镜像仓库stage('Build and Puah Image') &#123;<br>
sh '''<br>
docker login -u admin -p Harbor12345 harbor.uqp.com<br>
REPOSITORY=harbor.uqp.com/project/solo:$&#123;Tag&#125;<br>
cat > Dockerfile2 <<EOF<br>
FROM harbor.uqp.com/library/tomcat-85:latest<br>
RUN rm -rf /usr/local/tomcat/webapps/ROOT<br>
COPY target/*.war /usr/local/tomcat/webapps/ROOT.war<br>
CMD ["catalina.sh","run"]EOF<br>
docker build -t $REPOSITORY -f Dockerfile2 . <br>
docker push $REPOSITORY<br>
'''             #根据$Tag作为镜像版本号&#125;#部署到Docker主机stage('Deploy to Docker') &#123;<br>
sh '''<br>
REPOSITORY=harbor.uqp.com/project/solo:$&#123;Tag&#125;<br>
docker rm -f blog-solo | true<br>
docker image rm $REPOSITORY | true<br>
docker login -u amdin -p Harbor12345 harbor.uqp.com<br>
docker container run -d -v /usr/local/jdk:/usr/local/jdk --name blog-solo -p 88:8080 $REPOSITORY<br>
'''&#125;&#125; <br>
</pre><br>
<h3>发布测试</h3>Git仓库模拟提交代码创建tag：<br>
<pre class="prettyprint"># cd solo/# touch src/main/webapp/123.txt# git add .# git commit -m "touch 123.txt"# git tag 1.0.0# git push origin 1.0.0<br>
</pre><br>
Jenkins上执行任务：<br>
<br>带参数执行构建：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/0eee445cc4d5eddca6e87302ef6bc5d5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/0eee445cc4d5eddca6e87302ef6bc5d5.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/ab6292008715760673c9f7ecb1b2d46c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/ab6292008715760673c9f7ecb1b2d46c.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
到Docker主机上查看：<br>
<pre class="prettyprint"># docker ps -aCONTAINER ID        IMAGE                                COMMAND             CREATED             STATUS                       PORTS                  NAMES<br>
386b2097e507        harbor.uqp.com/project/solo:1.0.0    "catalina.sh run"   3 minutes ago       Exited (255) 2 minutes ago                          blog-solo<br>
</pre><br>
容器ID与Jenkins上一致，但意外退出，查看原因：<br>
<pre class="prettyprint"># docker logs 38[ERROR]-[2019-03-26 16:41:47]-[org.b3log.latke.Latkes:786]: Read skin [Pinghsu]'s  configuration failed: null<br>
[ERROR]-[2019-03-26 16:41:47]-[org.b3log.solo.SoloServletListener:316]: Can't load the default skins, please make sure skin [Pinghsu] is under skins directory and structure correctly<br>
</pre><br>
提示皮肤配置为空，因此容器启动不起来。整个过程中，maven构建这一步可能有误，但jenkins执行过程中未报错；也有可能是b3log官方仓库有问题。<br>
<br>查看Harbor是否有对应镜像：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210428/86eaaa1d8d815a2eb356957b33792d34.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210428/86eaaa1d8d815a2eb356957b33792d34.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
对应业务的Docker镜像已经上传到Harbor中。<br>
<br>大致过程是没有问题的，基本上可以实现业务基于Jenkins与Docker的自动化发布。后续有空再更新优化maven过程。作为自动化CI/CD流水线还是有很多优点的，例如：<br>
<ol><li>项目发布可视化，明确阶段，方便处理问题；</li><li>一个Jenkinsfile文件就可以管理整个项目生命周期；</li><li>代码版本管理方便，版本发布、回退一键完成。</li></ol><br>
<br>原文链接：<a href="https://blog.51cto.com/u_10272167/2730581" rel="nofollow" target="_blank">https://blog.51cto.com/u_10272167/2730581</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            