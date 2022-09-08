
---
title: 'Rainbond V5.8.1 版本发布 _ 支持应用导出非容器环境安装包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/5.8.1/en.png'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 06:32:00 GMT
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/5.8.1/en.png'
---

<div>   
<div class="content">
                                                                                            <p>Rainbond 5.8.1 支持在非容器环境中快速部署应用，监测应用的状态，同时全面支持英文化。</p> 
<h2>新增功能解读</h2> 
<h3>1. 支持应用导出非容器环境安装包</h3> 
<p>在实际使用场景中，我们常常会遇到以下几类问题。</p> 
<ul> 
 <li>在一些场景下，禁止使用容器类技术，开发的微服务应用如何部署</li> 
 <li>交付客户时，客户没有容器环境且资源有限，如何能不依赖平台部署应用</li> 
 <li>使用 Rainbond 简化开发测试，但是内部生产还使用传统方式部署，如何将开发的应用平滑迁移到非容器环境部署</li> 
</ul> 
<p>因此为了解决这几种场景下的应用部署问题，在企业视图->应用市场->导出应用模版中，Rainbond 支持了导出非容器环境安装包，该安装包安装包解压后，会包含你所有源码部署的业务组件以及各个组件的启动脚本。你可以在 Linux 操作系统中通过启动脚本部署起来你的应用。也可以在某个业务组件目录下单独运行业务模块，相关的组件配置仍然通过环境变量的形式定义。当前支持的语言有 Java-maven、Java-gradle、Java-jar、Java-war、NodeJS、Golang 以及 Html 静态页面。</p> 
<p>该导出包解压后，目录层级如下：</p> 
<pre><code>|-- go
|   |-- go.env
|   |-- go.sh
|   |-- go-slug.tgz
|-- java-maven
|   |-- java-maven.env
|   |-- java-maven.sh
|   |-- java-maven-slug.tgz
|-- source_code.sh
</code></pre> 
<p>以上是一个示例应用，里面包含了 go 和 java-maven 两个组件，其中 .env 结尾的定义了组件的环境变了、连接信息等，.sh 结尾的则为启动脚本，source_code.sh 这个脚本是应用的启动脚本。我们可以执行以下命令将组件直接运行起来。</p> 
<pre><code class="language-shell"># 直接运行该应用下所有组件，包含 go 和 java-maven 组件
./source_code.sh start
# 仅运行 java-maven 组件
cd ./java-maven
./java-maven.sh start
</code></pre> 
<p>运行效果如下:</p> 
<pre><code class="language-shell">[root@dev001 java-maven]# ./java-maven.sh start
Handling runtime environment ...  Done
The environment variable $MEMORY_SIZE was not identified,The Java process will not be optimized....
Handling custom environment ...  Done
Running app java-maven, you can check the logs in file java-maven.log
We will start your app with ==> java  -Dfile.encoding=UTF-8  -jar target/java-maven-demo-0.0.1.jar
Running app java-maven with process: 23368 java ...  Done

# 查看组件运行状态
[root@dev001 java-maven]# ./java-maven.sh status
AppName                        Status                         PID
java-maven                     Active(Running)                3958
</code></pre> 
<h3>2. 产品和文档支持英文</h3> 
<p>在之前也有部分用户提到过产品英文化的问题。因此为了让更多的用户体验到 Rainbond 管理应用的便捷体验。现在 Rainbond 全面支持中英文切换。</p> 
<p><img alt src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/5.8.1/en.png" referrerpolicy="no-referrer"></p> 
<h2>详细变更点</h2> 
<h3>新增功能</h3> 
<ul> 
 <li>【应用管理】支持非容器环境一键部署应用</li> 
 <li>【英文化】产品英文，并支持中英文切换</li> 
</ul> 
<h3>优化功能</h3> 
<ul> 
 <li>【安装】优化单机体验版安装流程，支持进度展示 #1294</li> 
 <li>【登录页】优化登录页风格</li> 
 <li>【应用管理】优化新增组件引导流程</li> 
</ul> 
<h3>BUG 修复</h3> 
<ul> 
 <li>【团队管理】修复团队人数统计错误的问题</li> 
 <li>【组件管理】修复 nodejs 前端项目构建命令错误的问题</li> 
 <li>【组件管理】修复 K8s 资源示例样式混乱及 CPU 单位错误的问题</li> 
 <li>【组件管理】修复从集群中导入资源，资源限制显示错误的问题</li> 
 <li>【组件管理】修复应用模版导出失败的问题 #1309</li> 
 <li>【报警管理】修复 rbd-worker 误报警的问题 #1296</li> 
 <li>【集群管理】修复单机版中集群 Dashboard 里 Ingress 资源不展示的问题 #1293</li> 
 <li>【应用管理】修复拓扑图权限和用户权限不一致问题 #1288</li> 
</ul> 
<h2>感谢</h2> 
<p>感谢 huzk、scrio、superjackwong、hanxinhisen、anchyobi、xuaiguo、zhengxu632、leiyu1982、stylesmile、runningbeanxl、MoXinQian、0haha、liwenson、ricky-rd、joychen-1991 等用户在社区中的参与与反馈，才能使产品变得更好，我们欢迎大家任何形式的参与和贡献。</p>
                                        </div>
                                      
</div>
            