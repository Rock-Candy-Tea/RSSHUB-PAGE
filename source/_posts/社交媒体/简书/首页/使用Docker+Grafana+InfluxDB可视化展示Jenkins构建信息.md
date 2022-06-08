
---
title: '使用Docker+Grafana+InfluxDB可视化展示Jenkins构建信息'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/3512339-b814a54be83ef116.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/3512339-b814a54be83ef116.png'
---

<div>   
<blockquote>
<p>20210410 Update docker-compose.yml.</p>
</blockquote>
<p></p>
<p></p>
环境搭建完成后，最终展示效果如下图所示：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1828" data-height="774"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-b814a54be83ef116.png" data-original-width="1828" data-original-height="774" data-original-format="image/png" data-original-filesize="220881" src="https://upload-images.jianshu.io/upload_images/3512339-b814a54be83ef116.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>docker-compose.yml</h2>
<p>内容如下：</p>
<pre><code>version: '3'
services:
    influxdb:
        image: influxdb:1.8.0
        container_name: influxdb
        restart: always
        ports:
            - "8086:8086"
        volumes:
            - /opt/docker/influxdb:/var/lib/influxdb
            - /etc/localtime:/etc/localtime
        hostname: influxdb
        environment:
            - ADMIN_USER=root
            - INFLUXDB_INIT_PWD=YOUR_PWD
            - PRE_CREATE_DB=jenkins
    chronograf:
        image: chronograf:1.8
        container_name: chronograf
        restart: always
        ports:
            - 8888:8888
        volumes:
            - /opt/docker/chronograf:/var/lib/chronograf
    grafana:
        image: grafana/grafana:7.3.0
        container_name: grafana
        restart: always
        links:
            - influxdb:influxdb
        ports:
            - "3000:3000"
        user: root
        volumes:
            - /etc/localtime:/etc/localtime
            - /opt/docker/grafana/grafana-data:/var/lib/grafana
            - /opt/docker/grafana/grafana-logs:/var/log/grafana
        environment:
            - INFLUXDB_HOST=influxdb
            - INFLUXDB_PORT=8086
            # 设置管理员登录密码, 默认为admin, 首次登录时需要进行修改
            - GF_SECURITY_ADMIN_PASSWORD=YOUR_PWD
            # 设置要安装的插件
            - GF_INSTALL_PLUGINS=grafana-piechart-panel
</code></pre>
<p>搭建过程中，有几个需要注意的地方，下面来稍微说说。</p>
<ol>
<li>不需要额外为influxDB容器开放8083端口，这是因为从InfluxDB 1.3以及之后的版本，已经取消了自带的web管理页面了，取而代之的是使用Chronograf；</li>
<li>创建Chronograf容器是可选的，容器启动后，访问:<a href="https://links.jianshu.com/go?to=HTTP%3A%2F%2FIP%3A8888" target="_blank">HTTP://IP:8888</a>，可以进入chronograf 控制台页面，如下：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1035" data-height="400"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-f0f450debbee4434.png" data-original-width="1035" data-original-height="400" data-original-format="image/png" data-original-filesize="21185" src="https://upload-images.jianshu.io/upload_images/3512339-f0f450debbee4434.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>第一项Connection URL不要用localhost，可能出现访问不通的情况，Username 和 Password可以保持空白后面再设置，Telegraf的默认数据库名称为<code>telegraf</code>，直接点击按钮下一步就好。</li>
<li>influxdb 容器启动成功后，进入容器内的<code>/usr/bin</code>目录，这里面存放了Influxdb相关的工具，如下。 当然也可以在Chronograf控制台页面进行数据库的CURD相关操作。</li>
</ol>
<pre><code>docker exec -it influxdb bash
cd /usr/bin
find | grep influx
./influx_stress
./influx_inspect
./influx
./influxd
./influx_tsm

# 查看版本
./influx -version
InfluxDB shell version: 1.8.0

# 进入Influxdb客户端命令行
./influx

# 创建jenkins数据库
`CREATE DATABASE  jenkins
</code></pre>
<ol start="4">
<li>grafana这里使用了7.3.0版本，如果从低版本迁移到高版本会有权限问题（坑!!），详见:<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgrafana.com%2Fdocs%2Fgrafana%2Flatest%2Finstallation%2Fdocker%2F%23migration-from-a-previous-version-of-the-docker-container-to-5-1-or-later" target="_blank">https://grafana.com/docs/grafana/latest/installation/docker/#migration-from-a-previous-version-of-the-docker-container-to-5-1-or-later</a>。 另外，考虑到要为Jenkins做一个构建成功率和构成失败率统计，所以为Grafana预安装了饼图插件，相关的方法在上面的链接中也有详细介绍。</li>
</ol>
<h2>Jenkins</h2>
<p></p>
<p></p>
Jenkins需要安装influxdb插件，承担数据采集的角色，在项目构建完成后，将本次构建信息推送到数据库中，后续Grafana配置好数据源后，就可以将数据进行可视化展示。<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="756" data-height="330"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-ae44440c43d92530.png" data-original-width="756" data-original-height="330" data-original-format="image/png" data-original-filesize="20433" src="https://upload-images.jianshu.io/upload_images/3512339-ae44440c43d92530.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>插件安装完成后，进入系统配置页面，设置下InfluxDB Targets：</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1529" data-height="546"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-7bc95adc1943950c.png" data-original-width="1529" data-original-height="546" data-original-format="image/png" data-original-filesize="53389" src="https://upload-images.jianshu.io/upload_images/3512339-7bc95adc1943950c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p></p>
<p></p>
配置保存成功后，进入项目配置页面，添加构建后操作。<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1101" data-height="328"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-5529760f3aa5bdb4.png" data-original-width="1101" data-original-height="328" data-original-format="image/png" data-original-filesize="26690" src="https://upload-images.jianshu.io/upload_images/3512339-5529760f3aa5bdb4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p></p>
<p></p>
当项目构建完成后，会自动上报十分详细的构建信息到数据库中，可以看到一些数据表已经自动被创建了。<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1156" data-height="501"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-93b0793519860139.png" data-original-width="1156" data-original-height="501" data-original-format="image/png" data-original-filesize="46304" src="https://upload-images.jianshu.io/upload_images/3512339-93b0793519860139.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>Grafana目录代理(可选)</h2>
<p>使用Nginx为grafana做了代理，以实现在公网下通过域名+"/grafana"的形式访问，点击查看<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgrafana.com%2Fdocs%2Finstallation%2Fbehind_proxy%2F" target="_blank">官方文档</a>，步骤如下：</p>
<ol>
<li>修改Nginx配置(nginx.conf)，红色部分为新增，<strong>proxy_pass后面一定要有"/"（用以去掉/grafana/匹配本身）</strong>
</li>
</ol>
<pre><code>server &#123;

listen 80;
root /usr/share/nginx/www;
index index.html index.htm;

location /grafana/ &#123;
proxy_pass http://localhost:3000/;
&#125;
&#125;
</code></pre>
<ol start="2">
<li>修改grafana配置(grafana.ini），由于grafana以容器形式启动，所以先拷贝配置文件到宿主机</li>
</ol>
<pre><code> docker cp grafana:/etc/grafana/grafana.ini /opt/docker/grafana-data/etc
</code></pre>
<p>然后修改配置文件中的以下内容：</p>
<pre><code>[server]
domain = 你的域名
root_url = %(protocol)s://%(domain)s/grafana/
</code></pre>
<p>配置文件修改完成后，重启容器再挂载宿主机配置文件目录到容器中。</p>
<pre><code>docker kill grafana
docker rm grafana
docker run  --user root -d --name grafana -p 3000:3000  -v /opt/docker/grafana-data/etc:/etc/grafana/ -v /opt/docker/grafana-data/grafana:/var/lib/grafana  grafana:mc
</code></pre>
<ol start="3">
<li>reload  nginx</li>
</ol>
<hr>
<h4>配置Grafana 数据源</h4>
<p></p>
<p></p>
数据源可以配置多个，配置项和Jenkins中一致就可以了。<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1347" data-height="850"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-7357cfe4fb74fb7b.png" data-original-width="1347" data-original-height="850" data-original-format="image/png" data-original-filesize="144732" src="https://upload-images.jianshu.io/upload_images/3512339-7357cfe4fb74fb7b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>Jenkins Dashboard</h4>
<p>Grafana提供了导入Dashboards模板的功能，在官网可以搜索很多别人已经实现的模板，我们只需要按需导入即可，十分方便，这里以Jmeter为例，进入官网 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgrafana.com%2Fgrafana%2Fdashboards%3Fdirection%3Dasc%26orderBy%3Dname%26search%3Djmeter" target="_blank">Grafana Dashboards 搜索</a>页面，点击搜索结果中的第一条：</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1384" data-height="485"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-f7bd0a98313bbc20.png" data-original-width="1384" data-original-height="485" data-original-format="image/png" data-original-filesize="95478" src="https://upload-images.jianshu.io/upload_images/3512339-f7bd0a98313bbc20.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
在页面右侧可以看到模板ID为5496，复制此ID，进入Grafana控制台页面，点击左侧的加号，选择Import然后输入模板ID，并导入即可，导入成功后，会自动新建一个 Jmeter Dashboard。<p></p>
<p>这里尝试去搜索Jenkins相关的模板，发现并没有符合我们要求的模板，所以后续是通过手动配置的方式来完成的，需要手动创建一个名为Jenkins的Dashboard，然后在进行后续操作。</p>
<p><strong>创建环境变量</strong><br>
采集到的数据是包括所有jenkins项目的构建数据，在利用这部分数据时，可以创建项目名称变量（projectName），这个变量实际就是Jenkins的Job Name，配置如下：</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1443" data-height="881"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-c1dce84e9f42b05a.png" data-original-width="1443" data-original-height="881" data-original-format="image/png" data-original-filesize="121873" src="https://upload-images.jianshu.io/upload_images/3512339-c1dce84e9f42b05a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<p></p>
<p></p>
保存完成后，在Dashboard页面，会发现多了一个名为"项目名称"的筛选项：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="687" data-height="454"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-824f36ee78346bb4.png" data-original-width="687" data-original-height="454" data-original-format="image/png" data-original-filesize="54134" src="https://upload-images.jianshu.io/upload_images/3512339-824f36ee78346bb4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>后续配置Panel时，在InfluxQL中可以通过$projectName的方式使用这个自定义的变量。</p>
<p>**Add Panel **<br>
下面是一些我用到视图类型以及对应的InlfuxQL，Visualization配置可以按照喜欢自行调整。</p>
<ul>
<li>Pie Chart</li>
</ul>
<pre><code># Title构建成功
SELECT count("build_result") FROM jenkins_data  WHERE ("build_result" = 'SUCCESS' AND "project_path" =~ /^$projectName$/) AND $timeFilter GROUP BY time($__interval) fill(null)

# Title 构建成功
SELECT count("build_result") FROM jenkins_data  WHERE ("build_result" = 'FAILURE' AND "project_path" =~ /^$projectName$/) AND $timeFilter GROUP BY time($__interval) fill(null)
</code></pre>
<ul>
<li>Graph</li>
</ul>
<pre><code># Title  构建耗时
SELECT "build_time" FROM "jenkins_data" WHERE ("project_path" =~ /^$projectName$/) AND $timeFilter ORDER BY time DESC tz('Asia/Shanghai')
</code></pre>
<ul>
<li>Gauge</li>
</ul>
<pre><code># Title 健康指数
SELECT project_build_health FROM jenkins_data  WHERE ("project_path" =~ /^$projectName$/) AND $timeFilter
</code></pre>
<ul>
<li>Table</li>
</ul>
<pre><code># Title 构建记录
SELECT "build_agent_name", "build_number", "build_result", "build_status_message", "build_time", "project_build_health" FROM "jenkins_data" WHERE ("project_path" =~ /^$projectName$/) AND $timeFilter GROUP BY "project_name" ORDER BY time DESC

</code></pre>
<hr>
<p>除了Jenkins构建结果外，Jmeter压测结果也可以通过后置处理器非常方便的采集到InfluxDB中，并利用Grafana进行展示。<br>
To be continued....</p>
  
</div>
            