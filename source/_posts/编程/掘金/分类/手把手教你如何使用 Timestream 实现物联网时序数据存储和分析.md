
---
title: '手把手教你如何使用 Timestream 实现物联网时序数据存储和分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260d0fbf49734be7b9b8193d87f4bacb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 00:23:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260d0fbf49734be7b9b8193d87f4bacb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Amazon Timestream 是一种快速、可扩展的无服务器时间序列数据库服务，适用于物联网和运营应用程序，使用该服务每天可以轻松存储和分析数万亿个事件，速度提高了 1000 倍，而成本仅为关系数据库的十分之一。通过将近期数据保留在内存中，并根据用户定义的策略将历史数据移至成本优化的存储层，Amazon Timestream 为客户节省了管理时间序列数据生命周期的时间和成本。Amazon Timestream 专门构建的查询引擎可用于访问和分析近期数据和历史数据，而无需在查询中显式指定数据是保存在内存中还是成本优化层中。Amazon Timestream 内置了时间序列分析函数，可以实现近乎实时地识别数据的趋势和模式。Amazon Timestream 是无服务器服务，可自动缩放以调整容量和性能，因此无需管理底层基础设施，可以专注于构建应用程序。</p>
<p>本文介绍通过 Timestream、Kinesis Stream 托管服务和 Grafana 和 Flink Connector 开源软件实现物联网（以 PM 2.5场景为示例）时序数据实时采集、存储和分析，其中包含部署架构、环境部署、数据采集、数据存储和分析，希望当您有类似物联网时序数据存储和分析需求的时候，能从中获得启发，助力业务发展。</p>
<h3 data-id="heading-0">架构</h3>
<p>Amazon Timestream 能够使用内置的分析函数（如平滑、近似和插值）快速分析物联网应用程序生成的时间序列数据。例如，智能家居设备制造商可以使用 Amazon Timestream 从设备传感器收集运动或温度数据，进行插值以识别没有运动的时间范围，并提醒消费者采取措施（例如减少热量）以节约能源。</p>
<p>本文物联网（以PM 2.5场景为示例），实现 PM2.5数据实时采集、时序数据存储和实时分析， 其中架构主要分成三大部分：</p>
<ul>
<li>实时时序数据采集：通过Python数据采集程序结合Kinesis Stream和Kinesis Data Analytics for Apache Flink connector 模拟实现从PM 2.5监控设备, 将数据实时采集数据到Timestream。</li>
<li>时序数据存储：通过Amazon Timestream时序数据库实现时序数据存储，设定内存和磁性存储（成本优化层）存储时长，可以实现近期数据保留在内存中，并根据用户定义的策略将历史数据移至成本优化的存储层。</li>
<li>实时时序数据分析：通过Grafana （安装Timesteam For Grafana插件）实时访问Timestream数据，通过Grafana丰富的分析图表形式，结合Amazon Timestream 内置的时间序列分析函数，可以实现近乎实时地识别物联网数据的趋势和模式。</li>
</ul>
<p>具体的架构图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260d0fbf49734be7b9b8193d87f4bacb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">部署环境</h3>
<h4 data-id="heading-2">1.1 创建 Cloudformation</h4>
<p>请使用自己帐号 (region 请选择 us-east-1)</p>
<p>下载 Github 上 Cloudformation Yaml 文件：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3D%252BS5Hg39EuWHmEPuG%252FL0IRA%253D%253D.R4GcqkQxZqDHX2Ss3MIqclIlG7d9NIo8P%252BZVJ3D2DqE%252F5hh4zRl5tzfKhnYndnBrApw6mbFuDwE3JNXnDuQVwOoRVJSO0%252B7XzERbZVaoNKw%253D" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?enc=%2BS5Hg39EuWHmEPuG%2FL0IRA%3D%3D.R4GcqkQxZqDHX2Ss3MIqclIlG7d9NIo8P%2BZVJ3D2DqE%2F5hh4zRl5tzfKhnYndnBrApw6mbFuDwE3JNXnDuQVwOoRVJSO0%2B7XzERbZVaoNKw%3D" ref="nofollow noopener noreferrer">git clone https://github.com/bingbingliu18/Timestream-pm25</a></p>
<p>Timestream-pm25目录中包含下面 Cloudformation 所用文件 timestream-short-new.yaml</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4a1012d8429454c9ea895763eb3f613~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58da03977f224d70a0cf370cab4be55f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9e1aafd011249cb9caedc89e33075f5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其它都选择缺省， 点击 Create Stack button.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d221d41b4ed5477f83ccaf62fd4648b3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dff85843feb54c0aa23ce6c144875525~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Cloud Formation 创建成功</p>
<h4 data-id="heading-3">1.2 连接到新建的Ec2堡垒机:</h4>
<p>修改证书文件权限</p>
<p>chmod 0600 [path to downloaded .pem file]</p>
<p>ssh -i [path to downloaded .pem file] ec2-user@[bastionEndpoint]</p>
<p>执行aws configure：</p>
<p>aws configure</p>
<p>default region name, 输入： “us-east-1”，其它选择缺省设置。</p>
<h4 data-id="heading-4">1.3 连接到 EC2堡垒机 安装相应软件</h4>
<p>设置时区</p>
<p><code>TZ='Asia/Shanghai'; export TZ</code></p>
<p>Install python3</p>
<p><code>sudo yum install -y python3</code></p>
<p>Install python3 pip</p>
<p><code>sudo yum install -y python3-pip</code></p>
<p>pip3 install boto3</p>
<p><code>sudo pip3 install boto3</code></p>
<p>pip3 install numpy</p>
<p><code>sudo pip3 install numpy</code></p>
<p>install git</p>
<p><code>sudo yum install -y git</code></p>
<h4 data-id="heading-5">1.4 下载 Github Timesteram Sample 程序库</h4>
<p><code>git clone https://github.com/awslabs/amazon-timestream-tools amazon-timestream-tools</code></p>
<h4 data-id="heading-6">1.5 安装 Grafana Server</h4>
<p>连接到 EC2堡垒机：</p>
<p><code>sudo vi /etc/yum.repos.d/grafana.repo</code></p>
<pre><code class="hljs language-ini copyable" lang="ini">For OSS releases:(拷贝以下内容到grafana.repo)

<span class="hljs-section">[grafana]</span>

<span class="hljs-attr">name</span>=grafana

<span class="hljs-attr">baseurl</span>=https://packages.grafana.com/oss/rpm

<span class="hljs-attr">repo_gpgcheck</span>=<span class="hljs-number">1</span>

<span class="hljs-attr">enabled</span>=<span class="hljs-number">1</span>

<span class="hljs-attr">gpgcheck</span>=<span class="hljs-number">1</span>

<span class="hljs-attr">gpgkey</span>=https://packages.grafana.com/gpg.key

<span class="hljs-attr">sslverify</span>=<span class="hljs-number">1</span>

<span class="hljs-attr">sslcacert</span>=/etc/pki/tls/certs/ca-bundle.crt
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装 grafana server:</p>
<p><code>sudo yum install -y grafana</code></p>
<p>启动 grafana server:</p>
<pre><code class="hljs language-vbscript copyable" lang="vbscript">sudo service grafana-<span class="hljs-built_in">server</span> start
sudo service grafana-<span class="hljs-built_in">server</span> status
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置 grafana server 在操作系统启动时 自动启动:</p>
<p><code>sudo /sbin/chkconfig --add grafana-server</code></p>
<h4 data-id="heading-7">1.6 安装 timestream Plugin</h4>
<p><code>sudo grafana-cli plugins install grafana-timestream-datasource</code></p>
<p>重启 grafana</p>
<p><code>sudo service grafana-server restart</code></p>
<h4 data-id="heading-8">1.7 配置 Grafana 要访问 Timesteam 服务所用的 IAM Role</h4>
<p>获取 IAM Role Name</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853edc7e99fe4c91b7061b36262e5147~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择 IAM 服务， 选择要修改的 role, role name:</p>
<p>timestream-iot-grafanaEC2rolelabview-us-east-1</p>
<p>修改 role trust relationship:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9368c7a853ae4f79afbbd812dd84c085~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>将 Policy document 全部选中， 替换成以下内容：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"Version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"2012-10-17"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"Statement"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-punctuation">&#123;</span>
      <span class="hljs-attr">"Sid"</span><span class="hljs-punctuation">:</span><span class="hljs-string">""</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"Effect"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Allow"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"Principal"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
        <span class="hljs-attr">"Service"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"ec2.amazonaws.com"</span>
      <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"Action"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"sts:AssumeRole"</span>
    <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
    <span class="hljs-punctuation">&#123;</span>
      <span class="hljs-attr">"Sid"</span><span class="hljs-punctuation">:</span><span class="hljs-string">""</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"Effect"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"Allow"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"Principal"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
        <span class="hljs-attr">"AWS"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"[请替换成CloudFormation output中的role arn]"</span>
      <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
      <span class="hljs-attr">"Action"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"sts:AssumeRole"</span>
    <span class="hljs-punctuation">&#125;</span> 
  <span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改后的 trust relationship:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b51abc071e404881a1ee195c819311~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">1.8登录到 Grafana server</h4>
<p>第一次登录到 Grafana Server:</p>
<ol>
<li>打开浏览器 访问 http://[Grafana server public ip]:3000</li>
<li>缺省的 Grafana Server 监听端口是： 3000 .</li>
</ol>
<p>如何获取 Ec2 Public IP 地址， 如下图所示， 访问 Cloudformation output：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84a3c7fc076f4fdeacc76d8746bace7b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>在登陆界面, 输入 username: admin; password:admin.(输入用户名和密码都是 admin)</li>
<li>点击 Log In.登陆成功后， 会收到提示修改密码</li>
</ol>
<h4 data-id="heading-10">1.9 Grafana server 中增加 Timestream 数据源</h4>
<p>增加 Timestream 数据源</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/978130474aa445f9a8058de0887f7d15~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">1.10 Grafana server 中配置 Timestream 数据源</h4>
<p>拷贝配置所需要 role ARN 信息 （从 cloudformation output tab）Default Region: us-east-1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00590b3ac69645b296cbec47fbfc7f84~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9344b8bed0be4c5a82395340c78dc159~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">IoT 数据存储</h3>
<h4 data-id="heading-13">2.1 创建 Timestream 数据库 iot</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/509507f8d17a4756935d6c37505d86d9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c695b16341374cd9a54f41390e4d1935~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">2.2 创建 Timestream 表 pm25</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9eba5dd0e134ce8af97786d0bfd6011~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">IoT 数据导入</h3>
<h4 data-id="heading-16">3.1安装 Flink connector to Timestream</h4>
<p>安装java8</p>
<p><code>sudo yum install -y java-1.8.0-openjdk*</code></p>
<p><code>java -version</code></p>
<p>安装debug info, otherwise jmap will throw exception</p>
<p><code>sudo yum --enablerepo='*-debug*' install -y java-1.8.0-openjdk-debuginfo</code></p>
<p>Install maven</p>
<pre><code class="hljs language-bash copyable" lang="bash">sudo wget https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo 
sudo sed -i s/<span class="hljs-variable">$releasever</span>/6/g /etc/yum.repos.d/epel-apache-maven.repo 
sudo yum install -y apache-maven 
mvn --version 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>change java version from 1.7 to 1.8</p>
<p><code>sudo update-alternatives --config java</code></p>
<p><code>sudo update-alternatives --config javac</code></p>
<p>安装 Apache Flink</p>
<p>最新的 Apache Flink 版本支持 Kinesis Data Analytics 是1.8.2.</p>
<ol>
<li>Create flink folder</li>
</ol>
<p><code>cd</code></p>
<p><code>mkdir flink</code></p>
<p><code>cd flink</code></p>
<ol>
<li>下载 Apache Flink version 1.8.2 源代码:</li>
</ol>
<p><code>wget https://archive.apache.org/dist/flink/flink-1.8.2/flink-1.8.2-src.tgz</code></p>
<ol>
<li>解压 Apache Flink 源代码:</li>
</ol>
<p><code>tar -xvf flink-1.8.2-src.tgz</code></p>
<ol>
<li>进入到 Apache Flink 源代码目录:</li>
</ol>
<p><code>cd flink-1.8.2</code></p>
<ol>
<li>Compile and install Apache Flink (这个编译时间比较长 需要大致20分钟):</li>
</ol>
<p><code>mvn clean install -Pinclude-kinesis -DskipTests</code></p>
<h4 data-id="heading-17">3.2 创建 Kinesis Data Stream Timestreampm25Stream</h4>
<p><code>aws kinesis create-stream --stream-name Timestreampm25Stream --shard-count 1</code></p>
<h4 data-id="heading-18">3.3 运行 Flink Connector 建立 Kinesis 连接到 Timestream:</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">cd</span>
<span class="hljs-built_in">cd</span> amazon-timestream-tools/integrations/flink_connector
mvn clean compile
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据采集过程中 请持续运行以下命令：</p>
<pre><code class="hljs language-ini copyable" lang="ini">mvn exec:java <span class="hljs-attr">-Dexec.mainClass</span>=<span class="hljs-string">"com.amazonaws.services.kinesisanalytics.StreamingJob"</span> -Dexec.args=<span class="hljs-string">"--InputStreamName 
Timestreampm25Stream --Region us-east-1 --TimestreamDbName iot --TimestreamTableName pm25"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3.4 准备 PM2.5演示数据:</h4>
<p>连接到 EC2堡垒机</p>
<p>下载5演示数据生成程序：</p>
<p><code>cd</code></p>
<p><code>mkdir pm25</code></p>
<p><code>cd pm25</code></p>
<ol>
<li>下载 Github 上数据采集 Python 程序：</li>
</ol>
<p><code>git clone https://github.com/bingbingliu18/Timestream-pm25</code></p>
<p><code>cd Timestream-pm25</code></p>
<ol>
<li>运行5演示数据生成程序 (python 程序2个参数 –region default: us-east-1; –stream default: Timestreampm25Stream)</li>
</ol>
<p>数据采集过程中 请持续运行以下命令：</p>
<p><code>python3 pm25_new_kinisis_test.py</code></p>
<h3 data-id="heading-20">IoT 数据分析</h3>
<h4 data-id="heading-21">4.1 登陆到 Grafana Server 创建仪表板和 Panel</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5d8f90bd9274c1cbde02e39eac53eb8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建 Dashboard 查询时 请设定时区为本地浏览器时区:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e9d35f1b8da424f92c3a008b22a9fa5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建新的 Panel:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/067c665e85d049a48d1dde983bd12929~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择要访问的数据源， 将要查询分析所执行的 SQL 语句粘贴到新的 Panel 中:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/676481b7817d436aa87c4c9aaef0e7f1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-22">4.2 创建时间数据分析仪表版 Dashboard PM2.5 Analysis 1(Save as PM2.5 Analysis 1)</h4>
<p><strong>4.2.1 查询北京各个监控站点PM2.5 平均值</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'fengtai_xiaotun'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> fengtai_xiaotou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'fengtai_yungang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> fengtai_yungang,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'daxing'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> daxing,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'wanshou'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> wanshou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'gucheng'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> gucheng,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'tiantan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> tiantan,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'yanshan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> yanshan,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'miyun'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> miyun,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'changping'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> changping,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'aoti'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> aoti,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'mengtougou'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> mentougou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'huairou'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> huairou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'haidian'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> haidian,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'nongzhan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> nongzhan,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'tongzhou'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> tongzhou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'dingling'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> dingling,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'yanqing'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> yanqing,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'guanyuan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> guanyuan,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'dongsi'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> dongsi,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'shunyi'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> shunyi
<span class="hljs-keyword">FROM</span> 
(<span class="hljs-keyword">SELECT</span> location, round(<span class="hljs-built_in">avg</span>(measure_value::<span class="hljs-type">bigint</span>),<span class="hljs-number">0</span>) <span class="hljs-keyword">as</span> avg_pm25
<span class="hljs-keyword">FROM</span> "iot"."pm25" 
<span class="hljs-keyword">where</span> measure_name<span class="hljs-operator">=</span><span class="hljs-string">'pm2.5'</span> 
<span class="hljs-keyword">and</span> city<span class="hljs-operator">=</span><span class="hljs-string">'Beijing'</span>
<span class="hljs-keyword">and</span> <span class="hljs-type">time</span> <span class="hljs-operator">>=</span> ago(<span class="hljs-number">30</span>s)
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> location,bin(<span class="hljs-type">time</span>,<span class="hljs-number">30</span>s)
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> avg_pm25 <span class="hljs-keyword">desc</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择图形显示 select Gauge</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe05511941a45799dd1c8cb14687025~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as Beijing PM2.5 analysis</p>
<p>Edit Panel Title：Beijing PM2.5 analysis</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/422949230c974da69a4964f767639953~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Dashboard PM2.5 analysis 1：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fc1270b63e14ed39272c4a91a917a48~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>4.2.2 查询上海一天内各个监控站点 PM2.5 平均值</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'songjiang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> songjiang,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'fengxian'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> fengxian, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'no 15 factory'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> No15_factory, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'xujing'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> xujing,
 <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'pujiang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> pujiang, 
 <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'putuo'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> putuo, 
 <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'shangshida'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> shangshida,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'jingan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> jingan, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'xianxia'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> xianxia, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'hongkou'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> hongkou, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'jiading'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> jiading, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'zhangjiang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> zhangjiang, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'miaohang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> miaohang, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'yangpu'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> yangpu, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'huinan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> huinan, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'chongming'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> chongming
<span class="hljs-keyword">From</span>(
<span class="hljs-keyword">SELECT</span> location, round(<span class="hljs-built_in">avg</span>(measure_value::<span class="hljs-type">bigint</span>),<span class="hljs-number">0</span>) <span class="hljs-keyword">as</span> avg_pm25
<span class="hljs-keyword">FROM</span> "iot"."pm25" 
<span class="hljs-keyword">where</span> measure_name<span class="hljs-operator">=</span><span class="hljs-string">'pm2.5'</span> 
<span class="hljs-keyword">and</span> city<span class="hljs-operator">=</span><span class="hljs-string">'Shanghai'</span>
<span class="hljs-keyword">and</span> <span class="hljs-type">time</span> <span class="hljs-operator">>=</span> ago(<span class="hljs-number">30</span>s)
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> location,bin(<span class="hljs-type">time</span>,<span class="hljs-number">30</span>s)
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> avg_pm25 <span class="hljs-keyword">desc</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01e118a532f44d299971ceed023b3b49~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as Shanghai PM2.5 analysis</p>
<p>Edit Panel Title：Shanghai PM2.5 analysis</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.3查询广州各个监控站点 PM2.5 平均值</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'panyu'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> panyu,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'commercial school'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> commercial_school, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'No 5 middle school'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> No_5_middle_school,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'guangzhou monitor station'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Guangzhou_monitor_station, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'nansha street'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Nansha_street, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'No 86 middle school'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> No_86_middle_school, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'luhu'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> luhu, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'nansha'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> nansha, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'tiyu west'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> tiyu_west, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'jiulong town'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> jiulong_town, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'huangpu'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Huangpu, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'baiyun'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Baiyun, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'maofeng mountain'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Maofeng_mountain, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'chong hua'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Chonghua, 
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'huadu'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> huadu
<span class="hljs-keyword">from</span>(
    <span class="hljs-keyword">SELECT</span> location, round(<span class="hljs-built_in">avg</span>(measure_value::<span class="hljs-type">bigint</span>),<span class="hljs-number">0</span>) <span class="hljs-keyword">as</span> avg_pm25
<span class="hljs-keyword">FROM</span> "iot"."pm25" 
<span class="hljs-keyword">where</span> measure_name<span class="hljs-operator">=</span><span class="hljs-string">'pm2.5'</span> 
<span class="hljs-keyword">and</span> city<span class="hljs-operator">=</span><span class="hljs-string">'Guangzhou'</span>
<span class="hljs-keyword">and</span> <span class="hljs-type">time</span> <span class="hljs-operator">>=</span> ago(<span class="hljs-number">30</span>s)
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> location,bin(<span class="hljs-type">time</span>,<span class="hljs-number">30</span>s)
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> avg_pm25 <span class="hljs-keyword">desc</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d05f347aa74346a264bf981d6c1bfe~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as Guangzhou PM2.5 analysis</p>
<p>Edit Panel Title：Guangzhou PM2.5 analysis</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.4 查询深圳各个监控站点 PM2.5 平均值</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'huaqiao city'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Huaqiao_city,
 <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'xixiang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> xixiang,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'guanlan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> guanlan,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'longgang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Longgang,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'honghu'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Honghu,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'pingshan'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Pingshan,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'henggang'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Henggang,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'minzhi'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Minzhi,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'lianhua'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Lianhua,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'yantian'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Yantian,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'nanou'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Nanou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> location <span class="hljs-operator">=</span> <span class="hljs-string">'meisha'</span> <span class="hljs-keyword">THEN</span> avg_pm25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Meisha
<span class="hljs-keyword">From</span>(
<span class="hljs-keyword">SELECT</span> location, round(<span class="hljs-built_in">avg</span>(measure_value::<span class="hljs-type">bigint</span>),<span class="hljs-number">0</span>) <span class="hljs-keyword">as</span> avg_pm25
<span class="hljs-keyword">FROM</span> "iot"."pm25" 
<span class="hljs-keyword">where</span> measure_name<span class="hljs-operator">=</span><span class="hljs-string">'pm2.5'</span> 
<span class="hljs-keyword">and</span> city<span class="hljs-operator">=</span><span class="hljs-string">'Shenzhen'</span>
<span class="hljs-keyword">and</span> <span class="hljs-type">time</span> <span class="hljs-operator">>=</span> ago(<span class="hljs-number">30</span>s)
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> location,bin(<span class="hljs-type">time</span>,<span class="hljs-number">30</span>s)
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> avg_pm25 <span class="hljs-keyword">desc</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/076447d177c942d9a1c8df4819108c5b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as Shenzhen PM2.5 analysis</p>
<p>Edit Panel Title：Shenzhen PM2.5 analysis</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.5 深圳华侨城时间序列分析(最近5分钟内 PM2.5分析)</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">select</span> location, CREATE_TIME_SERIES(<span class="hljs-type">time</span>, measure_value::<span class="hljs-type">bigint</span>) <span class="hljs-keyword">as</span> PM25 <span class="hljs-keyword">FROM</span> iot.pm25
<span class="hljs-keyword">where</span> measure_name<span class="hljs-operator">=</span><span class="hljs-string">'pm2.5'</span> 
<span class="hljs-keyword">and</span> location<span class="hljs-operator">=</span><span class="hljs-string">'huaqiao city'</span>
<span class="hljs-keyword">and</span> <span class="hljs-type">time</span> <span class="hljs-operator">>=</span> ago(<span class="hljs-number">5</span>m)
<span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> location
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择图形显示 select Lines; Select Points：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7acccffadfeb45fdb19053562bd79e08~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as Shen Zhen Huaqiao City PM2.5 analysis</p>
<p>Edit Panel Title： 深圳华侨城最近5分钟PM2.5分析</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.6找出过去2小时内深圳华侨城以30秒为间隔的平均 PM2.5值 （使用线性插值填充缺失的值）</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">WITH</span> binned_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s) <span class="hljs-keyword">AS</span> binned_timestamp, ROUND(<span class="hljs-built_in">AVG</span>(measure_value::<span class="hljs-type">bigint</span>), <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> avg_PM25
    <span class="hljs-keyword">FROM</span> "iot".pm25
    <span class="hljs-keyword">WHERE</span> measure_name <span class="hljs-operator">=</span> <span class="hljs-string">'pm2.5'</span>
        <span class="hljs-keyword">AND</span> location<span class="hljs-operator">=</span><span class="hljs-string">'huaqiao city'</span>
        <span class="hljs-keyword">AND</span> <span class="hljs-type">time</span> <span class="hljs-operator">></span> ago(<span class="hljs-number">2</span>h)
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s)
), interpolated_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> location,
        INTERPOLATE_LINEAR(
            CREATE_TIME_SERIES(binned_timestamp, avg_PM25),
                SEQUENCE(<span class="hljs-built_in">min</span>(binned_timestamp), <span class="hljs-built_in">max</span>(binned_timestamp), <span class="hljs-number">30</span>s)) <span class="hljs-keyword">AS</span> interpolated_avg_PM25
    <span class="hljs-keyword">FROM</span> binned_timeseries
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> location
)
<span class="hljs-keyword">SELECT</span> <span class="hljs-type">time</span>, ROUND(<span class="hljs-keyword">value</span>, <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> interpolated_avg_PM25
<span class="hljs-keyword">FROM</span> interpolated_timeseries
<span class="hljs-keyword">CROSS</span> <span class="hljs-keyword">JOIN</span> <span class="hljs-built_in">UNNEST</span>(interpolated_avg_PM25)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择图形显示 select Lines：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dd098b5e24345328282842cabbe3f75~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as Shen Zhen Huaqiao City PM2.5 analysis 1</p>
<p>Edit Panel Title： 过去2小时深圳华侨城平均PM2.5值 （使用线性插值填充缺失值）</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.7 过去5分钟内所有城市 PM2.5平均值排名 （线性插值）</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">SELECT</span> <span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Shanghai'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Shanghai,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Beijing'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Beijing,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Guangzhou'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Guangzhou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Shenzhen'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Shenzhen,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Hangzhou'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Hangzhou,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Nanjing'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Nanjing,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Chengdu'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Chengdu,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Chongqing'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Chongqing,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Tianjin'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Tianjin,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Shenyang'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Shenyang,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Sanya'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Sanya,
<span class="hljs-keyword">CASE</span> <span class="hljs-keyword">WHEN</span> city <span class="hljs-operator">=</span> <span class="hljs-string">'Lasa'</span> <span class="hljs-keyword">THEN</span> inter_avg_PM25 <span class="hljs-keyword">ELSE</span> <span class="hljs-keyword">NULL</span> <span class="hljs-keyword">END</span> <span class="hljs-keyword">AS</span> Lasa
<span class="hljs-keyword">from</span>(
<span class="hljs-keyword">WITH</span> binned_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> city,location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s) <span class="hljs-keyword">AS</span> binned_timestamp, ROUND(<span class="hljs-built_in">AVG</span>(measure_value::<span class="hljs-type">bigint</span>), <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> avg_PM25
    <span class="hljs-keyword">FROM</span> "iot".pm25
    <span class="hljs-keyword">WHERE</span> measure_name <span class="hljs-operator">=</span> <span class="hljs-string">'pm2.5'</span>
        <span class="hljs-keyword">AND</span> <span class="hljs-type">time</span> <span class="hljs-operator">></span> ago(<span class="hljs-number">5</span>m)
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> city,location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s)
), interpolated_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> city,location,
        INTERPOLATE_LINEAR(
            CREATE_TIME_SERIES(binned_timestamp, avg_PM25),
                SEQUENCE(<span class="hljs-built_in">min</span>(binned_timestamp), <span class="hljs-built_in">max</span>(binned_timestamp), <span class="hljs-number">30</span>s)) <span class="hljs-keyword">AS</span> interpolated_avg_PM25
    <span class="hljs-keyword">FROM</span> binned_timeseries
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> city,location
), all_location_interpolated <span class="hljs-keyword">as</span> (
<span class="hljs-keyword">SELECT</span> city,location,<span class="hljs-type">time</span>, ROUND(<span class="hljs-keyword">value</span>, <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> interpolated_avg_PM25
<span class="hljs-keyword">FROM</span> interpolated_timeseries
<span class="hljs-keyword">CROSS</span> <span class="hljs-keyword">JOIN</span> <span class="hljs-built_in">UNNEST</span>(interpolated_avg_PM25))
<span class="hljs-keyword">select</span> city,<span class="hljs-built_in">avg</span>(interpolated_avg_PM25) <span class="hljs-keyword">AS</span> inter_avg_PM25
<span class="hljs-keyword">from</span> all_location_interpolated
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> city
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> <span class="hljs-built_in">avg</span>(interpolated_avg_PM25) <span class="hljs-keyword">desc</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择 Panel 图形类型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b302a587a8064d309e5104ec5e5c6868~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50bc0d040c4c4aefaf18a489be4b66b7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as all city analysis 1</p>
<p>Edit Panel Title： 过去5分钟所有城市PM2.5平均值</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.8 过去5分钟内 PM2.5最高的十个采集点（线性插值）</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">WITH</span> binned_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> city,location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s) <span class="hljs-keyword">AS</span> binned_timestamp, ROUND(<span class="hljs-built_in">AVG</span>(measure_value::<span class="hljs-type">bigint</span>), <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> avg_PM25
    <span class="hljs-keyword">FROM</span> "iot".pm25
    <span class="hljs-keyword">WHERE</span> measure_name <span class="hljs-operator">=</span> <span class="hljs-string">'pm2.5'</span>
        <span class="hljs-keyword">AND</span> <span class="hljs-type">time</span> <span class="hljs-operator">></span> ago(<span class="hljs-number">5</span>m)
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> city,location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s)
), interpolated_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> city,location,
        INTERPOLATE_LINEAR(
            CREATE_TIME_SERIES(binned_timestamp, avg_PM25),
                SEQUENCE(<span class="hljs-built_in">min</span>(binned_timestamp), <span class="hljs-built_in">max</span>(binned_timestamp), <span class="hljs-number">30</span>s)) 
                <span class="hljs-keyword">AS</span> interpolated_avg_PM25
    <span class="hljs-keyword">FROM</span> binned_timeseries
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> city,location
), interpolated_cross_join <span class="hljs-keyword">as</span> (
<span class="hljs-keyword">SELECT</span> city,location,<span class="hljs-type">time</span>, ROUND(<span class="hljs-keyword">value</span>, <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> interpolated_avg_PM25
<span class="hljs-keyword">FROM</span> interpolated_timeseries
<span class="hljs-keyword">CROSS</span> <span class="hljs-keyword">JOIN</span> <span class="hljs-built_in">UNNEST</span>(interpolated_avg_PM25))
<span class="hljs-keyword">select</span> city,location, <span class="hljs-built_in">avg</span>(interpolated_avg_PM25) <span class="hljs-keyword">as</span> avg_PM25_loc
<span class="hljs-keyword">from</span> interpolated_cross_join
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> city,location
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> avg_PM25_loc <span class="hljs-keyword">desc</span>
limit <span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择 Table</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3943e7503044d67b0eb4cfaf3164361~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as all city analysis 2</p>
<p>Edit Panel Title：过去5分钟内 PM2.5最高的十个采集点（线性插值）</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p><strong>4.2.9 过去5分钟内 PM2.5最低的十个采集点（线性插值）</strong></p>
<p>New Panel</p>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-keyword">WITH</span> binned_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> city,location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s) <span class="hljs-keyword">AS</span> binned_timestamp, ROUND(<span class="hljs-built_in">AVG</span>(measure_value::<span class="hljs-type">bigint</span>), <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> avg_PM25
    <span class="hljs-keyword">FROM</span> "iot".pm25
    <span class="hljs-keyword">WHERE</span> measure_name <span class="hljs-operator">=</span> <span class="hljs-string">'pm2.5'</span>
        <span class="hljs-keyword">AND</span> <span class="hljs-type">time</span> <span class="hljs-operator">></span> ago(<span class="hljs-number">5</span>m)
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> city,location, BIN(<span class="hljs-type">time</span>, <span class="hljs-number">30</span>s)
), interpolated_timeseries <span class="hljs-keyword">AS</span> (
    <span class="hljs-keyword">SELECT</span> city,location,
        INTERPOLATE_LINEAR(
            CREATE_TIME_SERIES(binned_timestamp, avg_PM25),
                SEQUENCE(<span class="hljs-built_in">min</span>(binned_timestamp), <span class="hljs-built_in">max</span>(binned_timestamp), <span class="hljs-number">30</span>s)) 
                <span class="hljs-keyword">AS</span> interpolated_avg_PM25
    <span class="hljs-keyword">FROM</span> binned_timeseries
    <span class="hljs-keyword">GROUP</span> <span class="hljs-keyword">BY</span> city,location
), interpolated_cross_join <span class="hljs-keyword">as</span> (
<span class="hljs-keyword">SELECT</span> city,location,<span class="hljs-type">time</span>, ROUND(<span class="hljs-keyword">value</span>, <span class="hljs-number">2</span>) <span class="hljs-keyword">AS</span> interpolated_avg_PM25
<span class="hljs-keyword">FROM</span> interpolated_timeseries
<span class="hljs-keyword">CROSS</span> <span class="hljs-keyword">JOIN</span> <span class="hljs-built_in">UNNEST</span>(interpolated_avg_PM25))
<span class="hljs-keyword">select</span> city,location, <span class="hljs-built_in">avg</span>(interpolated_avg_PM25) <span class="hljs-keyword">as</span> avg_PM25_loc
<span class="hljs-keyword">from</span> interpolated_cross_join
<span class="hljs-keyword">group</span> <span class="hljs-keyword">by</span> city,location
<span class="hljs-keyword">order</span> <span class="hljs-keyword">by</span> avg_PM25_loc <span class="hljs-keyword">asc</span>
limit <span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择 Table</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01c92866a19d4ae1a5d2172c96123821~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Save Panel as all city analysis 3</p>
<p>Edit Panel Title：过去5分钟内 PM2.5最低的十个采集点（线性插值）</p>
<p>Save Dashboard PM2.5 analysis 1</p>
<p>设置仪表板 每5秒钟刷新一次:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd306e73c97c424d9791ed58fb0ec256~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77f19ab769c64a7fb6c1e706318ea7b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>本 blog 着重介绍通过 Timestream、Kinesis Stream 托管服务和 Grafana 实现物联网（以 PM 2.5场景为示例）时序数据实时采集、存储和分析，其中包含部署架构、环境部署、数据采集、数据存储和分析，希望当您有类似物联网时序数据存储和分析需求的时候，有所启发，实现海量物联网时序数据高效管理、挖掘物联网数据中蕴含的规律、模式和价值，助力业务发展。</p>
<h4 data-id="heading-23">附录</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3D1KpVUhCY53%252Bc7Diw%252F5rNpw%253D%253D.87kF56DZut5nK1doCstVnJNq01L2CKoohIAVixTvDUff4%252B%252F9f8NxNMc%252F55o69kT1Hkb8L3YVr65rKnEiSudWxeH4cjtRURrWfB5Vr4WfZFIFTvJmJ5LOodYJrkURW3Ty" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?enc=1KpVUhCY53%2Bc7Diw%2F5rNpw%3D%3D.87kF56DZut5nK1doCstVnJNq01L2CKoohIAVixTvDUff4%2B%2F9f8NxNMc%2F55o69kT1Hkb8L3YVr65rKnEiSudWxeH4cjtRURrWfB5Vr4WfZFIFTvJmJ5LOodYJrkURW3Ty" ref="nofollow noopener noreferrer">《Amazon Timestream 开发人员指南》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3Ds9nDiypA9ZLHF8Ga98a1iw%253D%253D.A8QQrEFYmVFmzGSOBvAMW2wNk4SxXYOsrylMigm%252BLqlMyfWm80fcy73bLbeS8PZnZekA0Qo6D7bgUCvd7CNw%252FjkRDXDRJxacCWoI8sd9wIM%253D" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?enc=s9nDiypA9ZLHF8Ga98a1iw%3D%3D.A8QQrEFYmVFmzGSOBvAMW2wNk4SxXYOsrylMigm%2BLqlMyfWm80fcy73bLbeS8PZnZekA0Qo6D7bgUCvd7CNw%2FjkRDXDRJxacCWoI8sd9wIM%3D" ref="nofollow noopener noreferrer">《AWS Timestream 开发程序示例》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.segmentfault.com%2F%3Fenc%3DVwSO1%252Falw9z%252FwT%252BeDHWsjg%253D%253D.CYsr1w5B%252Fzgbf1oDRlegnSq1I3JOqD3r4R%252Ft2MnTUIAvh%252BW1%252FZCZF4uRyOZyJZgPjdBVblh%252FPJXKxqsTHAxN1LvlmqpPSLx8UhXK1wVlcA2PC3fGiIT8MRcNcxrG%252Bt88%252B3pScsBIJfAyHHYcvMnc%252FA%253D%253D" target="_blank" rel="nofollow noopener noreferrer" title="https://link.segmentfault.com/?enc=VwSO1%2Falw9z%2FwT%2BeDHWsjg%3D%3D.CYsr1w5B%2Fzgbf1oDRlegnSq1I3JOqD3r4R%2Ft2MnTUIAvh%2BW1%2FZCZF4uRyOZyJZgPjdBVblh%2FPJXKxqsTHAxN1LvlmqpPSLx8UhXK1wVlcA2PC3fGiIT8MRcNcxrG%2Bt88%2B3pScsBIJfAyHHYcvMnc%2FA%3D%3D" ref="nofollow noopener noreferrer">《AWS Timestream 与 Grafana 集成示例》</a></p>
<h4 data-id="heading-24">本篇作者</h4>
<p><strong>刘冰冰</strong></p>
<p>AWS 数据库解决方案架构师，负责基于 AWS 的数据库解决方案的咨询与架构设计，同时致力于大数据方面的研究和推广。在加入 AWS 之前曾在 Oracle 工作多年，在数据库云规划、设计运维调优、DR 解决方案、大数据和数仓以及企业应用等方面有丰富的经验。</p>
<p>更多信息，请访问链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Faws.amazon.com%2Fcn%2Fgetting-started%2Fdatabases%2Fget-started%2F%3Fnc%3Dsn%26loc%3D4%26trk%3Dfab55528-7c2e-4517-b90e-65b760ecfc1c%26sc_channel%3Del" target="_blank" rel="nofollow noopener noreferrer" title="https://aws.amazon.com/cn/getting-started/databases/get-started/?nc=sn&loc=4&trk=fab55528-7c2e-4517-b90e-65b760ecfc1c&sc_channel=el" ref="nofollow noopener noreferrer">aws.amazon.com/cn/getting-…</a></p></div>  
</div>
            