
---
title: '企业级日志平台新秀 Graylog，比 ELK 轻量多了'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/461c167c911c4954d1337378407eca5a.png'
author: Dockone
comments: false
date: 2021-11-26 12:11:49
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/461c167c911c4954d1337378407eca5a.png'
---

<div>   
<br>【编者的话】服务日志收集方案：Filebeat + Graylog！<br>
<br>当我们公司内部部署很多服务以及测试、正式环境的时候，查看日志就变成了一个非常刚需的需求了。是多个环境的日志统一收集，然后使用 <code class="prettyprint">Nginx</code> 对外提供服务，还是使用专用的日志收集服务 <code class="prettyprint">ELK</code> 呢？这就变成了一个问题！而 <code class="prettyprint">Graylog</code> 作为整合方案，使用 <code class="prettyprint">Elasticsearch</code> 来存储，使用 <code class="prettyprint">MongoDB</code> 来缓存，并且还有带流量控制的（<code class="prettyprint">throttling</code>），同时其界面查询简单易用且易于扩展。所以，使用 <code class="prettyprint">Graylog</code> 成为了不二之选，为我们省了不少心。<br>
<h3>Filebeat 工具介绍</h3><h4>Filebeat 日志文件托运服务</h4><code class="prettyprint">Filebeat</code> 是一个日志文件托运工具，在你的服务器上安装客户端后，<code class="prettyprint">Filebeat</code> 会自动监控给定的日志目录或者指定的日志文件，追踪读取这些文件，不停的读取，并且转发这些信息到 <code class="prettyprint">Elasticsearch</code> 或者 <code class="prettyprint">Logstarsh</code> 或者 <code class="prettyprint">Graylog</code> 中存放。<br>
<h4>Filebeat 工作流程介绍</h4>当你安装并启用 <code class="prettyprint">Filebeat</code> 程序的时候，它会启动一个或多个探测器（<code class="prettyprint">prospectors</code>）去检测你指定的日志目录或文件，对于探测器找出的每一个日志文件，<code class="prettyprint">Filebeat</code> 都会启动一个收割进程（<code class="prettyprint">harvester</code>），每一个收割进程读取一个日志文件的最新内容，并发送这些新的日志数据到处理程序（<code class="prettyprint">spooler</code>），处理程序会集合这些事件，最后 <code class="prettyprint">Filebeat</code> 会发送集合的数据到你指定的地址上去（我们这里就是发送给 <code class="prettyprint">Graylog</code> 服务了）。<br>
<h4>Filebeat 图示理解记忆</h4>我们这里不适用 <code class="prettyprint">Logstash</code> 服务，主要是因为 <code class="prettyprint">Filebeat</code> 相比于 <code class="prettyprint">Logstash</code> 更加轻量级。当我们需要收集信息的机器配置或资源并不是特别多时，且并没有那么复杂的时候，还是建议使用 <code class="prettyprint">Filebeat</code> 来收集日志。日常使用中，<code class="prettyprint">Filebeat</code> 的安装部署方式多样且运行十分稳定。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/461c167c911c4954d1337378407eca5a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/461c167c911c4954d1337378407eca5a.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图示服务架构理解记忆</em><br>
<h3>Filebeat 配置文件</h3>配置 Filebeat 工具的核心就是如何编写其对应的配置文件！<br>
<br>对应 <code class="prettyprint">Filebeat</code> 工具的配置主要是通过编写其配置文件来控制的，对于通过 <code class="prettyprint">rpm</code> 或者 <code class="prettyprint">deb</code> 包来安装的情况，配置文件默认会存储在，<code class="prettyprint">/etc/filebeat/filebeat.yml</code> 这个路径下面。而对于，对于 <code class="prettyprint">MAC</code> 或者 <code class="prettyprint">Win</code> 系统来说，请查看解压文件中相关文件，其中都有涉及。<br>
<br>下面展示了 <code class="prettyprint">Filebeat</code> 工具的主配置文件，注释信息中都对其各个字段含义进行了详细的解释，我这里就不再赘述了。需要注意的是，我们将日志的输入来源统统定义去读取 <code class="prettyprint">inputs.d</code> 目录下的所有 <code class="prettyprint">yml</code> 配置。所以，我们可以更加不用的服务（测试、正式服务）来定义不同的配置文件，根据物理机部署的实际情况具体配置。<br>
<pre class="prettyprint"># 配置输入来源的日志信息<br>
# 我们合理将其配置到了 inputs.d 目录下的所有 yml 文件<br>
filebeat.config.inputs:<br>
enabled: true<br>
path: $&#123;path.config&#125;/inputs.d/*.yml<br>
# 若收取日志格式为 json 的 log 请开启此配置<br>
# json.keys_under_root: true<br>
<br>
# 配置 Filebeat 需要加载的模块<br>
filebeat.config.modules:<br>
path: $&#123;path.config&#125;/modules.d/*.yml<br>
reload.enabled: false<br>
<br>
setup.template.settings:<br>
index.number_of_shards: 1<br>
<br>
# 配置将日志信息发送那个地址上面<br>
output.logstash:<br>
hosts: ["11.22.33.44:5500"]<br>
<br>
# output.file:<br>
#   enable: true<br>
<br>
processors:<br>
- add_host_metadata: ~<br>
- rename:<br>
  fields:<br>
    - from: "log"<br>
      to: "message"<br>
- add_fields:<br>
  target: ""<br>
  fields:<br>
    # 加 Token 是为了防止无认证的服务上 Graylog 服务发送数据<br>
    token: "0uxxxxaM-1111-2222-3333-VQZJxxxxxwgX "<br>
</pre><br>
下面展示一个简单的 <code class="prettyprint">inputs.d</code> 目录下面的 <code class="prettyprint">yml</code> 配置文件的具体内容，其主要作用就是配置单独服务的独立日志数据，以及追加不同的数据 <code class="prettyprint">tag</code> 类型。<br>
<pre class="prettyprint"># 收集的数据类型<br>
- type: log<br>
enabled: true<br>
# 日志文件的路径地址<br>
paths:<br>
- /var/log/supervisor/app_escape_worker-stderr.log<br>
- /var/log/supervisor/app_escape_prod-stderr.log<br>
symlinks: true<br>
# 包含的关键字信息<br>
include_lines: ["WARNING", "ERROR"]<br>
# 打上数据标签<br>
tags: ["app", "escape", "test"]<br>
# 防止程序堆栈信息被分行识别<br>
multiline.pattern: '^\[?[0-9]...&#123;3&#125;'<br>
multiline.negate: true<br>
multiline.match: after<br>
<br>
# 需要配置多个日志时可加多个 type 字段<br>
- type: log<br>
enabled: true<br>
......<br>
</pre><br>
需要注意的是，针对于不同的日志类型，<code class="prettyprint">filebeat</code>  还提供了不同了模块来配置不同的服务日志以及其不同的模块特性，比如我们常见的 <code class="prettyprint">PostgreSQl</code>、<code class="prettyprint">Redis</code>、<code class="prettyprint">Iptables</code> 等。<br>
<pre class="prettyprint"># iptables<br>
- module: iptables<br>
log:<br>
enabled: true<br>
var.paths: ["/var/log/iptables.log"]<br>
var.input: "file"<br>
<br>
# postgres<br>
- module: postgresql<br>
log:<br>
enabled: true<br>
var.paths: ["/path/to/log/postgres/*.log*"]<br>
<br>
# nginx<br>
- module: nginx<br>
access:<br>
enabled: true<br>
var.paths: ["/path/to/log/nginx/access.log*"]<br>
error:<br>
enabled: true<br>
var.paths: ["/path/to/log/nginx/error.log*"] <br>
</pre><br>
<h3>Graylog 服务介绍</h3><h4>Graylog 日志监控系统</h4><code class="prettyprint">Graylog</code> 是一个开源的日志聚合、分析、审计、展现和预警工具。在功能上来说，和 <code class="prettyprint">ELK</code> 类似，但又比 <code class="prettyprint">ELK</code> 要简单很多。依靠着更加简洁，高效，部署使用简单的优势很快受到许多人的青睐。当然，在扩展性上面确实没有比 <code class="prettyprint">ELK</code> 好，但是其有商业版本可以选择。<br>
<h4>Graylog 工作流程介绍</h4>部署 <code class="prettyprint">Graylog</code> 最简单的架构就是单机部署，复杂的也是部署集群模式，架构图示如下所示。我们可以看到其中包含了三个组件，分别是 <code class="prettyprint">Elasticsearch</code>、<code class="prettyprint">MongoDb</code>  和 <code class="prettyprint">Graylog</code>。其中，<code class="prettyprint">Elasticsearch</code> 用来持久化存储和检索日志文件数据（IO 密集），<code class="prettyprint">MongoDb</code> 用来存储关于 <code class="prettyprint">Graylog</code> 的相关配置，而 <code class="prettyprint">Graylog</code> 来提供 Web 界面和对外接口的（CPU 密集）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/40d112180b18ae74a6b3ec4605c3ca05.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/40d112180b18ae74a6b3ec4605c3ca05.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>最小化单机部署</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/cd887f57d3ee3cdaa47f7e25917fab7e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/cd887f57d3ee3cdaa47f7e25917fab7e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>最优化集群部署</em><br>
<h3>Graylog 组件功能</h3><strong>配置 Graylog 服务的核心就是理解对应组件的功能以及其运作方式！</strong><br>
<br>简单来讲，<code class="prettyprint">Input</code> 表示日志数据的来源，对不同来源的日志可以通过 <code class="prettyprint">Extractors</code> 来进行日志的字段转换，比如将 <code class="prettyprint">Nginx</code> 的状态码变成对应的英文表述等。然后，通过不同的标签类型分组成不用的 <code class="prettyprint">Stream</code>，并将这些日志数据存储到指定的 <code class="prettyprint">Index</code> 库中进行持久化保存。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/c3ae32f04f420d8879d429989ffcd4b8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/c3ae32f04f420d8879d429989ffcd4b8.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/ca12777036353d5a28517fed7c10fd9f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/ca12777036353d5a28517fed7c10fd9f.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Graylog中的核心服务组件</em><br>
<br><code class="prettyprint">Graylog</code> 通过 <code class="prettyprint">Input</code> 搜集日志，每个 <code class="prettyprint">Input</code> 单独配置 <code class="prettyprint">Extractors</code> 用来做字段转换。<code class="prettyprint">Graylog</code> 中日志搜索的基本单位是 <code class="prettyprint">Stream</code>，每个 <code class="prettyprint">Stream</code> 可以有自己单独的 <code class="prettyprint">Elastic Index Set</code>，也可以共享一个 <code class="prettyprint">Index Set</code>。<br>
<br><code class="prettyprint">Extractor</code> 在 <code class="prettyprint">System/Input</code> 中配置。<code class="prettyprint">Graylog</code> 中很方便的一点就是可以加载一条日志，然后基于这个实际的例子进行配置并能直接看到结果。内置的 <code class="prettyprint">Extractor</code> 基本可以完成各种字段提取和转换的任务，但是也有些限制，在应用里写日志的时候就需要考虑到这些限制。<code class="prettyprint">Input</code> 可以配置多个 <code class="prettyprint">Extractors</code>，按照顺序依次执行。<br>
<br>系统会有一个默认的 <code class="prettyprint">Stream</code>，所有日志默认都会保存到这个 <code class="prettyprint">Stream</code> 中，除非匹配了某个 <code class="prettyprint">Stream</code>，并且这个 <code class="prettyprint">Stream</code> 里配置了不保存日志到默认 <code class="prettyprint">Stream</code>。可以通过菜单 <code class="prettyprint">Streams</code> 创建更多的 <code class="prettyprint">Stream</code>，新创建的 <code class="prettyprint">Stream</code> 是暂停状态，需要在配置完成后手动启动。<code class="prettyprint">Stream</code> 通过配置条件匹配日志，满足条件的日志添加 <code class="prettyprint">stream ID</code> 标识字段并保存到对应的 <code class="prettyprint">Elastic Index Set</code> 中。<br>
<br><code class="prettyprint">Index Set</code> 通过菜单 <code class="prettyprint">System/Indices</code> 创建。日志存储的性能，可靠性和过期策略都通过 <code class="prettyprint">Index Set</code> 来配置。性能和可靠性就是配置 <code class="prettyprint">Elastic Index</code> 的一些参数，主要参数包括，<code class="prettyprint">Shards</code> 和 <code class="prettyprint">Replicas</code>。<br>
<br>除了上面提到的日志处理流程，<code class="prettyprint">Graylog</code> 还提供了 <code class="prettyprint">Pipeline</code> 脚本实现更灵活的日志处理方案。这里不详细阐述，只介绍如果使用 <code class="prettyprint">Pipelines</code> 来过滤不需要的日志。下面是丢弃 <code class="prettyprint">level > 6</code> 的所有日志的 <code class="prettyprint">Pipeline Rule</code> 的例子。从数据采集（<code class="prettyprint">input</code>），字段解析（<code class="prettyprint">extractor</code>），分流到 <code class="prettyprint">stream</code>，再到 <code class="prettyprint">Pipeline</code> 的清洗，一气呵成，无需在通过其他方式进行二次加工。<br>
<br><code class="prettyprint">Sidecar</code> 是一个轻量级的日志采集器，通过访问 <code class="prettyprint">Graylog</code> 进行集中式管理，支持 <code class="prettyprint">Linux</code> 和 <code class="prettyprint">windows</code>  系统。<code class="prettyprint">Sidecar</code> 守护进程会定期访问 <code class="prettyprint">Graylog</code> 的 <code class="prettyprint">REST API</code> 接口获取 <code class="prettyprint">Sidecar</code> 配置文件中定义的标签（<code class="prettyprint">tag</code>），<code class="prettyprint">Sidecar</code> 在首次运行时会从 <code class="prettyprint">Graylog</code> 服务器拉取配置文件中指定标签（<code class="prettyprint">tag</code>）的配置信息同步到本地。目前 <code class="prettyprint">Sidecar</code> 支持 <code class="prettyprint">NXLog</code>，<code class="prettyprint">Filebeat</code> 和 <code class="prettyprint">Winlogbeat</code>。他们都通过 <code class="prettyprint">Graylog</code> 中的 <code class="prettyprint">web</code> 界面进行统一配置，支持 <code class="prettyprint">Beats</code>、<code class="prettyprint">CEF</code>、<code class="prettyprint">Gelf</code>、<code class="prettyprint">Json API</code>、<code class="prettyprint">NetFlow</code> 等输出类型。<code class="prettyprint">Graylog</code> 最厉害的在于可以在配置文件中指定 <code class="prettyprint">Sidecar</code> 把日志发送到哪个 <code class="prettyprint">Graylog</code> 群集，并对 <code class="prettyprint">Graylog</code> 群集中的多个 <code class="prettyprint">input</code> 进行负载均衡，这样在遇到日志量非常庞大的时候，<code class="prettyprint">Graylog</code> 也能应付自如。<br>
<pre class="prettyprint">rule "discard debug messages"<br>
when<br>
to_long($message.level) > 6<br>
then<br>
drop_message();<br>
end<br>
</pre><br>
日志集中保存到 <code class="prettyprint">Graylog</code> 后就可以方便的使用搜索了。不过有时候还是需要对数据进行近一步的处理。主要有两个途径，分别是直接访问 <code class="prettyprint">Elastic</code> 中保存的数据，或者通过 <code class="prettyprint">Graylog</code> 的 <code class="prettyprint">Output</code> 转发到其它服务。<br>
<h3>服务安装和部署</h3><strong>主要介绍部署 Filebeat + Graylog 的安装步骤和注意事项！</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/af74714acbb3fefe51fd050792b6249b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/af74714acbb3fefe51fd050792b6249b.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>使用 Graylog 来收集日志</em><br>
<h4>部署 Filebeat 工具</h4>官方提供了多种的部署方式，包括通过 <code class="prettyprint">rpm</code> 和 <code class="prettyprint">deb</code> 包安装服务，以及源代码编译的方式安装服务，同时包括了使用 <code class="prettyprint">Docker</code> 或者 <code class="prettyprint">kubernetes</code> 的方式安装服务。我们根据自己的实际需要，进行安装即可。<br>
<pre class="prettyprint"># Ubuntu(deb)<br>
$ curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.8.1-amd64.deb<br>
$ sudo dpkg -i filebeat-7.8.1-amd64.deb<br>
$ sudo systemctl enable filebeat<br>
$ sudo service filebeat start<br>
</pre><br>
<pre class="prettyprint"># 使用 Docker 启动<br>
docker run -d --name=filebeat --user=root \<br>
--volume="./filebeat.docker.yml:/usr/share/filebeat/filebeat.yml:ro" \<br>
--volume="/var/lib/docker/containers:/var/lib/docker/containers:ro" \<br>
--volume="/var/run/docker.sock:/var/run/docker.sock:ro" \<br>
docker.elastic.co/beats/filebeat:7.8.1 filebeat -e -strict.perms=false \<br>
-E output.elasticsearch.hosts=["elasticsearch:9200"] <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/7f90012690b528bc0a322d899c5f90b2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/7f90012690b528bc0a322d899c5f90b2.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>使用 Graylog 来收集日志</em><br>
<h4>部署 Graylog 服务</h4>我们这里主要介绍使用 <code class="prettyprint">Docker</code> 容器来部署服务，如果你需要使用其他方式来部署的话，请自行查看官方文档对应章节的安装部署步骤。在服务部署之前，我们需要给 <code class="prettyprint">Graylog</code> 服务生成等相关信息，生成部署如下所示：<br>
<pre class="prettyprint"># 生成 password_secret 密码（最少 16 位）<br>
$ sudo apt install -y pwgen<br>
$ pwgen -N 1 -s 16<br>
zscMb65...FxR9ag<br>
<br>
# 生成后续 Web 登录时所需要使用的密码<br>
$ echo -n "Enter Password: " && head -1 </dev/stdin | tr -d '\n' | sha256sum | cut -d" " -f1<br>
Enter Password: zscMb65...FxR9ag<br>
77e29e0f...557515f<br>
</pre><br>
生成所需密码信息之后，我们将如下 <code class="prettyprint">yml</code> 信息保存到 <code class="prettyprint">docker-comopse.yml</code> 文件中，使用 <code class="prettyprint">docker-compose</code> 命令启动该服务，即可完成部署。之后，通过浏览器访问对应服务器地址的 <code class="prettyprint">9000</code> 端口，即可登录主页 。<br>
<pre class="prettyprint">version: "3"<br>
<br>
services:<br>
mongo:<br>
restart: on-failure<br>
container_name: graylog_mongo<br>
image: "mongo:3"<br>
volumes:<br>
  - "./mongodb:/data/db"<br>
networks:<br>
  - graylog_network<br>
<br>
elasticsearch:<br>
restart: on-failure<br>
container_name: graylog_es<br>
image: "elasticsearch:6.8.5"<br>
volumes:<br>
  - "./es_data:/usr/share/elasticsearch/data"<br>
environment:<br>
  - http.host=0.0.0.0<br>
  - transport.host=localhost<br>
  - network.host=0.0.0.0<br>
  - "ES_JAVA_OPTS=-Xms512m -Xmx5120m"<br>
ulimits:<br>
  memlock:<br>
    soft: -1<br>
    hard: -1<br>
deploy:<br>
  resources:<br>
    limits:<br>
      memory: 12g<br>
networks:<br>
  - graylog_network<br>
<br>
graylog:<br>
restart: on-failure<br>
container_name: graylog_web<br>
image: "graylog/graylog:3.3"<br>
ports:<br>
  - 9000:9000 # Web 服务提供的访问端口<br>
  - 5044:5044 # Filebeat 工具提供端口<br>
  - 12201:12201 # GELF TCP<br>
  - 12201:12201/udp # GELF UDP<br>
  - 1514:1514 # Syslog TCP<br>
  - 1514:1514/udp # Syslog UDP<br>
volumes:<br>
  - "./graylog_journal:/usr/share/graylog/data/journal"<br>
environment:<br>
  - GRAYLOG_PASSWORD_SECRET=zscMb65...FxR9ag<br>
  - GRAYLOG_ROOT_PASSWORD_SHA2=77e29e0f...557515f<br>
  - GRAYLOG_HTTP_EXTERNAL_URI=http://11.22.33.44:9000/<br>
  - GRAYLOG_TIMEZONE=Asia/Shanghai<br>
  - GRAYLOG_ROOT_TIMEZONE=Asia/Shanghai<br>
networks:<br>
  - graylog<br>
depends_on:<br>
  - mongo<br>
  - elasticsearch<br>
<br>
networks:<br>
graylog_network:<br>
driver: bridge<br>
</pre><br>
需要注意的是，<code class="prettyprint">GELF</code>（<code class="prettyprint">Graylog Extended Log Format</code>）的 <code class="prettyprint">input</code> 模式可以接受结构化的事件，支持压缩和分块。恰好，<code class="prettyprint">Docker</code> 服务的 <code class="prettyprint">log-driver</code> 驱动原生提供了 <code class="prettyprint">GELF</code> 的支持。只需要我们在 <code class="prettyprint">Graylog</code> 的 <code class="prettyprint">system/inputs</code> 下面创建对应的 <code class="prettyprint">input</code> 之后，启动容器时候指定 <code class="prettyprint">log-driver</code>，就可以将容器内的输出都会发送到 <code class="prettyprint">Graylog</code> 里面了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/b96e39ea2872dd9f2508e3e7c97506a8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/b96e39ea2872dd9f2508e3e7c97506a8.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>使用 Graylog 来收集日志</em><br>
<pre class="prettyprint"># [docker] 启动容器指定地址和 driver<br>
docker run --rm=true \<br>
--log-driver=gelf \<br>
--log-opt gelf-address=udp://11.22.33.44:12201 \<br>
--log-opt tag=myapp \<br>
myapp:0.0.1<br>
</pre><br>
<pre class="prettyprint"># [docker-compose] 启动使用方式<br>
version: "3"<br>
services:<br>
redis:<br>
restart: always<br>
image: redis<br>
container_name: "redis"<br>
logging:<br>
  driver: gelf<br>
  options:<br>
    gelf-address: udp://11.22.33.44:12201<br>
    tag: "redis"<br>
......<br>
</pre><br>
<h3>Graylog 界面功能</h3><strong>主要介绍 Graylog 界面的相关功能和对应特点！</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/ea938939a2e90493106d0d24b2f84d63.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/ea938939a2e90493106d0d24b2f84d63.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/e35e0f63df8b00dfe16ea588d736c216.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/e35e0f63df8b00dfe16ea588d736c216.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/a0cfb04dbf20a22eb1385a6baa30cc42.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/a0cfb04dbf20a22eb1385a6baa30cc42.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/63760721c2ddd20407b0c3cacdc136db.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/63760721c2ddd20407b0c3cacdc136db.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211122/bc43f1b3d80c42a7ed7394251c8155e9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211122/bc43f1b3d80c42a7ed7394251c8155e9.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Graylog界面功能</em><br>
<br>参考文章：<br>
<ul><li><a href="https://www.elastic.co/guide/en/beats/filebeat/current/index.html" rel="nofollow" target="_blank">https://www.elastic.co/guide/e ... .html</a></li><li><a href="https://www.cnblogs.com/kerwinC/p/6227768.html" rel="nofollow" target="_blank">https://www.cnblogs.com/kerwinC/p/6227768.html</a></li><li><a href="https://medium.com/@doitian/" rel="nofollow" target="_blank">https://medium.com/@doitian/graylog-</a>集中日志系统-1f715bb7998c</li><li><a href="https://zhuanlan.zhihu.com/p/113761931" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/113761931</a></li></ul><br>
<br>文章链接：<a href="https://www.escapelife.site/posts/38c81b25.html" rel="nofollow" target="_blank">https://www.escapelife.site/posts/38c81b25.html</a>，作者：Escape
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            