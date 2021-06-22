
---
title: '通过 Docker Compose 管理我的个人服务器'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/04/29/9fb50f2ac726f70e8747dc11ffabbbf7.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Fri, 18 Jun 2021 10:16:34 GMT
thumbnail: 'https://cdn.sspai.com/2021/04/29/9fb50f2ac726f70e8747dc11ffabbbf7.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><p>我拥有自己的一台云服务器，主要用来部署一些我个人所需要的服务。由于使用了 Docker Compose，相比起直接部署，更加便于管理，备份等。</p><p>本文只是个人的一些实践。我不是计算机专业的，也没有系统学习过相关知识，所有的内容都是自己自学摸索或网络搜索学习得来的，因此难免存在一些差错，在一些专有名词的使用上也可能会出现错误，欢迎讨论与指正。</p><p>文中一些终端的截图是我 ssh 到服务器上截取的，由于没有太多配置（服务器上一般也用不到这些美化配置），因此颜色可能比较单调。</p><h2>使用的原因</h2><p>我个人刚开始接触云服务器时，可以说只是计算机的小白，完全没有系统化地学习过，甚至能够理解的操作也仅限于复制黏贴等简单操作，就连写一个脚本都要每次上网搜索如判断语句的写法。</p><p>当时我购买服务器的理由我记得不是很清楚了，但是很明显，我能干的事情并不多，能独立解决的问题更少，因此一开始只能够完全按照文档所说的内容进行安装，直接复制黏贴，修改一下文档提到需要修改的部分，同时很多时候也会因为一些细节原因，安装失败。有时候一个很简单的应用我要折腾一整天才能部署成功。</p><p>直到有一天，我看到了一篇介绍 <a href="https://chengpengzhao.com/2020-08-03-vps-neng-yong-lai-zuo-shi-me" target="_blank">服务器搭建服务的文章</a>，里面介绍可以通过 Docker Compose 来进行管理。在此之前，我只是知道 Docker 与 Docker Compose，但是从未使用过。因此我也借此机会了解了一下它的基础操作，并尝试了一番，发现相比起我之前的那些步骤，确实方便了许多。</p><h3>优势</h3><p>通过 Docker 搭配上 Docker Compose，可以只依靠一个文件，就管理好整个服务器的应用，不需要在迁移或出现问题重装了系统后，如果没有完整系统的备份，只能一个一个应用按照文档重装，这样很可能会出现这样那样的一些小意外，需要耗费大量的时间。同时完整的备份需要消耗大量的空间，而服务器上的空间购买起来也并不便宜，下载到本地会由于带宽的限制需要不少的时间。因此综合来看使用 Docker 进行管理会更加方便。</p><h3>缺点</h3><p>Docker 具有一定的学习成本，需要一定的时间来熟悉 Docker 的操作。同时，Docker 的每一个 image 都需要占据不小的空间，且运行的服务如果较多，对 CPU 的压力也不小，这对于个人服务器的性能与容量都提出了一定的要求。</p><p>另外，由于运行的应用还需要备份一些数据文件，因此也不是真的只有一个文件需要备份而已，只是恢复的时候会比较简单，相对而言备份文件的大小会更小。所以，具体最终选择的选项还是需要进行一定的权衡来决定。</p><h3>适合什么情形</h3><p>那么，什么情况下才需要配置 Docker 来管理自己的服务器呢？</p><p>我个人认为，如果这台服务器上只有 web 服务器与一两个简单的应用，且用户并不熟悉 Docker，或是服务器性能有限，无法支持 Docker 部署多个应用，那么其实直接在宿主机上跑这些应用也是十分可行的。不过如果应用数量较多，那么宿主机的空间可能会变得杂乱起来，各种配置可能会出现干扰，导致出现问题时的重新部署耗时也会显著增加。这时就可以考虑使用 Docker 来进行部署与管理了。</p><p>当然，这些只是我个人使用下来的一些体验，由于没有系统学习或是培训过，可能会与实际产生一定的偏差。具体还是要看每个人不同的使用方式与习惯再决定是否要使用 Docker。</p><p>下文中所有操作，操作系统为 Ubuntu 20.04 LTS，用户名为 ubuntu，家目录为 <code>/home/ubuntu</code>，具有 sudo 权限，使用的 shell 为 bash，只开放了 80(http)、443(https) 和 ssh 修改过的非默认端口这三个端口。Docker 相关的内容在家目录下的 <code>docker</code> 目录，备份在家目录下的 <code>backup</code> 目录。所有的域名都使用 <code>example.com</code> 代替。</p><h2>安装与配置简介</h2><h3>安装</h3><p>首先需要在服务器上安装 Docker。对于不同的系统，安装的方式也不尽相同，具体可以参考 <a href="https://docs.docker.com/engine/install/" target="_blank">官网</a> 上的具体操作步骤。最好参照官网的步骤，而不是直接使用默认源里的版本，因为那个很可能是旧版本。</p><p>安装完成后，为了能够更方便地使用与管理，建议一起安装 Docker Compose。建议按照 Docker Compose <a href="https://docs.docker.com/compose/install/">官方建议的安装方式</a> 进行安装，即</p><pre class="language-shell"><code>sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose</code></pre><p>在完成安装后，可以通过加上 <code>--version</code> 的方式判断是否安装成功。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/04/29/9fb50f2ac726f70e8747dc11ffabbbf7.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/04/29/9fb50f2ac726f70e8747dc11ffabbbf7.png" referrerpolicy="no-referrer"><figcaption>截图上的版本号并不一定是最新的</figcaption></figure><p>这样就是安装成功了，之后如果是国内的服务器，则可以通过修改镜像源来加快拉取镜像的速度。</p><p>这里以 <a href="https://mirrors.sjtug.sjtu.edu.cn/docs/docker-registry" target="_blank">上海交通大学源</a> 为例，在 <code>/etc/docker/daemon.json</code> 文件中（如果没有就新建）加入</p><pre class="language-null"><code>&#123;
  "registry-mirrors": ["https://docker.mirrors.sjtug.sjtu.edu.cn"]
&#125;</code></pre><h3>配置文件说明</h3><p>Docker Compose 需要一个名为 <code>docker-compose.yml</code> 的文件来进行配置。由于一般只是使用别人打包好的镜像，因此不需要学习如何自己创建一个 image。</p><p>首先来熟悉一下配置文件的格式。它使用的是 <code>YAML</code> 格式，非常简单易懂，通过不同的缩进来区别层级关系。</p><p>在第一行，需要通过 <code>version: "3"</code> 来指明需要的最低 Docker Compose 的版本。一般 3 就足够了，如果需要其他的可以参照 <a href="https://docs.docker.com/compose/compose-file/" target="_blank">官方表格</a> 来进行选择。</p><p>随后，需要一行 <code>services:</code> 来囊括所需要的一切服务。以下的内容如果没有具体指明，均写在 <code>services</code> 的子集中。</p><p>接下来就是一个个服务了，每一个都是单独的一个单元，命名可以随意，但是不要重复，例如两个数据库可以分别命名为 <code>service1sql</code> 与 <code>service2sql</code>。这里通过 RSSHub 的<a href="https://github.com/DIYgod/RSSHub/blob/master/docker-compose.yml" target="_blank">官方示例</a>来简单介绍一下具体的写法。</p><pre class="language-null"><code>version: '3'
services:
  rsshub:
    image: diygod/rsshub
    restart: always
    ports:
      - '1200:1200'
    environment:
      NODE_ENV: production
      CACHE_TYPE: redis
      REDIS_URL: 'redis://redis:6379/'
      PUPPETEER_WS_ENDPOINT: 'ws://browserless:3000'
    depends_on:
      - redis
      - browserless
  browserless:
  # See issue 6680
    image: browserless/chrome:1.43-chrome-stable
    restart: always
  redis:
    image: redis:alpine
    restart: always
    volumes:
      - redis-data:/data
volumes:
redis-data:</code></pre><p>其中的 <code>rsshub</code>，<code>browserless</code> 和 <code>redis</code> 都是服务的名称。每一项服务下面都有 <code>image</code>，指的是具体在构建时需要拉取的镜像，所有的镜像可以在 <a href="https://hub.docker.com/" target="_blank">官网</a> 上搜索找到，一般下面还会有 <code>README</code> 文件指导如何使用配置。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/4aebab937fd0a13d38294d17f8cdbf30.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/4aebab937fd0a13d38294d17f8cdbf30.png" referrerpolicy="no-referrer"><figcaption>Docker Hub 上搜索到的 RSSHub</figcaption></figure><p>在 <code>browserless</code> 中镜像名称后面还有一个冒号，后面所接的内容是具体拉取镜像的标签，可以理解为不同的版本，也可以在网站上查到。</p><p><code>restart: always</code> 指的是在服务停止后是否重新启动，而 <code>always</code> 指的就是会不断尝试重启，保证服务一直在线。它还有其他不同的选项，不过一般用 <code>always</code> 就可以满足绝大部分的需求了。如果不写，那默认是 <code>no</code>，即退出时不会自动重启。</p><p><code>ports</code> 是端口映射，就是将容器的端口与宿主机的端口进行绑定。绑定后，宿主机的这一端口就会被占用，因此不能进行重复绑定。其中的 <code>1200:1200</code> 中，左侧的为宿主机的端口号，右侧的则是容器的。如此一来，通过访问 <code>localhost:1200</code>，即可访问到 <code>rsshub</code> 中的 1200 端口，也就能够访问其服务了。</p><p><code>volumes</code> 是为了持久化 Docker 中的文件数据而存在的。它能够将容器中的文件或目录映射到宿主机中来，双方互相都能够访问到这部分文件或目录。备份也就是针对通过 <code>volumes</code> 绑定来的文件目录。不然，只要这一服务重启，所有之前进行的操作都将会被消除。绑定依旧是左侧为宿主机，右侧为容器。这里可以是相对路径，也可以是绝对路径。</p><p>另外还可以写为卷标，即 <code>redis</code> 中的写法。这样，需要在 <code>services</code> 同级添加一项 <code>volumes</code> 来指定卷标。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/04/29/92ef4fbf0008f17293dec2c2d18291e9.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/04/29/92ef4fbf0008f17293dec2c2d18291e9.png" referrerpolicy="no-referrer"></figure><p><code>environment</code>  里指定需要的环境变量。具体哪些需要指定一般会在镜像的介绍页面指出，按照自己的需要书写。</p><p><code>depends_on</code>  用于指定依赖，即指定该服务必须需要的其他服务，镜像的介绍页一般也会指出具体的内容。</p><p><code>docker-compose.yml</code> 文件基本就是这么一些内容，接下来就可以进行实际操作了。</p><h2>具体配置</h2><h3>权限设置</h3><p>首先，Docker 默认只有 <code>root</code> 账户有权使用。由于在服务器上使用 <code>root</code> 并不是一个好习惯，因此建议将一个普通用户加入 <code>docker</code> 用户组来进行后续的操作。</p><pre class="language-shell"><code>sudo usermod -a -G docker username</code></pre><p>我先介绍一下我的配置方式。</p><h3>nginx</h3><p>我会通过一个 <code>nginx</code> 容器，使用反向代理来管理所有的容器，因此只需要映射该镜像的 80 与 443 端口到宿主机即可，不会过多占用宿主机的端口。</p><pre class="language-null"><code>web:
    image: nginx:alpine
    restart: always
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - ./nginx/conf:/etc/nginx/sites
      - ./nginx/ssl/cert:/etc/letsencrypt
    ports:
      - "80:80"
      - "443:443"</code></pre><p>这样其他的服务就能够不用对外暴露端口了。之后简单编写一下 nginx 的配置文件，对于 nginx 熟悉的可以直接跳过了。</p><p>由于 nginx 代理的每个应用我都写了单独的一个 conf 文件，因此需要先在默认配置中把它们 include 进来。</p><pre class="language-null"><code>include /etc/nginx/sites/*.conf;</code></pre><p>随后，在宿主机中的 <code>nginx/conf</code> 文件夹中，每个应用配置一个 conf 文件</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/05/01/987ffb34e8ec2278aa9d89d2c3671314.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/05/01/987ffb34e8ec2278aa9d89d2c3671314.png" referrerpolicy="no-referrer"></figure><p>而 conf 文件中的内容大致为</p><pre class="language-null"><code>server&#123;
  listen 80;
  server_name example.com;
  index  index.php index.html index.htm;

  location / &#123;
    proxy_pass http://name:8888;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  &#125;

&#125;</code></pre><p>而如果如下文一样配置了 https 的话，那么配置建议改为</p><pre class="language-null"><code>server&#123;
  listen 443 ssl;
  server_name example.com;
  index  index.php index.html index.htm;
  client_max_body_size 128M;
  ssl_certificate  /etc/letsencrypt/live/example.com/fullchain.pem;
  ssl_certificate_key  /etc/letsencrypt/live/example.com/privkey.pem;

  location / &#123;
    proxy_pass http://name:8888;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  &#125;

&#125;

server &#123;
  listen 80;
  server_name example.com;
  rewrite ^(.*)$ https://example.com;
&#125;</code></pre><p>其中，<code>example.com</code> 如果是<strong>本地部署</strong>的话，需要改为 <code>127.0.0.1</code>， 而其他需要根据不同的 Docker 配置进行更换。需要注意的是，<code>name</code> 需要改为应用在 <code>docker-compose.yml</code> 中被起的名字，后面的 <code>8888</code> 也是需要根据应用占用的端口的需要进行配置。</p><p>如果需要更加具体的配置可以考虑学习一下 <a href="https://nginx.org/en/docs" target="_blank">nginx</a>。</p><h3>Let's Encrypt</h3><p>由于需要保证数据传输的安全性，开启 https 是必然的。SSL 证书可以通过 Let's Encrypt 非常简单快捷地申请到。当然，前提是需要拥有域名。域名相关的内容这里就不详细展开介绍了，如果没有域名，那么接下来这段就不必参照我的做法来操作了。</p><p>申请 Let's Encrypt 的证书最简单的方法是通过 <code>certbot</code> 来进行。只需要根据在 <a href="https://certbot.eff.org/" target="_blank">官网</a> 上，选择相应的系统与使用的应用，即可获取到操作步骤。默认情况下，是每个域名都对应一张证书，不过也可以选择申请通配符证书，更加方便。</p><p>首先，在 <a href="https://certbot.eff.org/docs/using.html#dns-plugins" target="_blank">用户文档</a> 中查看是否支持自己使用的 DNS 服务商。如果没有，则可以直接跳转到手动申请了。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/7ba5eea6350776bb2761c264d9d6f774.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/7ba5eea6350776bb2761c264d9d6f774.png" referrerpolicy="no-referrer"><figcaption>目前支持的服务商</figcaption></figure><p>在选择了支持的服务商后，首先需要申请执行所需的 api token。这一步骤每个服务商都不尽相同，因此可以在指南中点开自己使用的服务商，并按照说明操作。不过需要注意的是，文档只有英文版，没有中文。</p><p>申请完成后，不要急着关闭页面，一般来说申请到的 token 只会显示一次，如果关掉页面而没有保存下来的话，将无法找回。因此千万记得关闭前保存好自己的 token。另外，建议跟着文档选择权限，一般不需要给予完整权限。</p><p>然后，创建一个文件，在其中填写下申请到的 api token。这里以我使用的 cloudflare 为例。不同的服务商请根据文档填写。</p><pre class="language-null"><code># Cloudflare API token used by Certbot
dns_cloudflare_api_token = 0123456789abcdef0123456789abcdef01234567</code></pre><p>这里我将文件保存为 <code>cloudflare.ini</code>。文件名称没有关系，只是在后面脚本中记得更改即可。</p><p>准备完成后，就是</p><pre class="language-shell"><code>#!/bin/bash
docker run -it --rm --name certbot \
  -v "/home/ubuntu/docker/nginx/ssl/cert:/etc/letsencrypt" \
  -v "/home/ubuntu/docker/nginx/ssl/var:/var/lib/letsencrypt" \
  -v "/home/ubuntu/docker/nginx/ssl/var:/var/lib/letsencrypt" \
  -v "/home/ubuntu/docker/nginx/ssl/cloudflare.ini:/cloudflare.ini" \
  -v "/home/ubuntu/docker/nginx/conf:/etc/nginx/conf.d" \
certbot/dns-cloudflare certonly \
  --dns-cloudflare \
  --dns-cloudflare-credentials /cloudflare.ini \
  -d *.example.com \
  -d example.com \</code></pre><p>运行这个脚本，就可以全自动化部署 SSL 证书了。</p><p>如果只申请 <code>*.example.com</code>，是不会自动申请 <code>example.com</code> 这个域名的，因此还要额外加上。</p><p>如果是<strong>手动申请</strong>，那么需要将脚本改为</p><pre class="language-shell"><code>#!/bin/bash
docker run -it --rm --name certbot \
certbot/certbot certonly \
  --manual</code></pre><p>并按照运行后所说明进行后续操作。</p><p>要注意的是，需要在部署完成后，运行 <code>docker-compose restart</code>，重新部署的证书才能生效。</p><p>如果一切顺利，那么在打开网页后，域名左侧会有一把小锁，点开可以查看自己的证书。 Let's Encrypt 证书的有效期是 90 天，要注意证书的过期时间，定时运行脚本。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/57d524946b137cfbddc72c2070f46843.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/57d524946b137cfbddc72c2070f46843.png" referrerpolicy="no-referrer"></figure><figure class="image ss-img-wrapper image_resized" style="width:413px;"><img src="https://cdn.sspai.com/2021/06/18/c8c94a1a857dfdb604b715561ba079a0.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/c8c94a1a857dfdb604b715561ba079a0.png" referrerpolicy="no-referrer"></figure><h3>其他</h3><p>配置完 nginx 后，基础内容就已经完成了，接下来就是找到自己喜欢的，感兴趣的容器，并按照 README 进行配置，由于步骤各不相同，这里就不再赘述了。最后，为每一个应用写一份 nginx 的配置文件，再启动容器，就能通过浏览器或其他形式访问了。</p><h2>使用操作</h2><h3>命令简介</h3><p>简单介绍几条会使用到的命令。命令分两类，一类是 Docker 的命令，还有一类是 Docker Compose 的命令。区别在于命令是 <code>docker</code> 还是 <code>docker-compose</code>。由于这里主要介绍的是 Docker Compose，因此介绍的命令也以 Docker Compose 的为主。</p><p><code>docker-compose</code> 命令会向上递归搜索 <code>docker-compose.yml</code> 文件来执行，因此并不一定需要每次都回到根目录来执行命令。</p><ol><li><code>docker-compose config</code>：验证并查看配置文件。建议在执行以下命令前先执行该命令，确保不会出现错误。</li><li><code>docker-compose up</code>：根据配置文件，创建并启动容器。这一步会自动拉取所需要的镜像。可以在后面加上 <code>-d</code> 来使该命令在后台运行。</li><li><code>docker-compose down</code>：根据配置文件停止运行容器。</li><li><code>docker-compose start/stop/restart/pull [image name]</code>：启动/停止/重启/拉取镜像。如果不添加名称则根据配置文件操作所有镜像。</li><li><code>docker-compose ps</code>：列出所有运行中的容器。可以用来查看运行的情况。</li></ol><p>因此一次完整的操作所需要的步骤包括：</p><ol><li>编辑好配置文件以及各镜像所需的配置。</li><li>先通过 <code>docker-compose config</code> 来检查配置是否出错。</li><li>使用 <code>docker-compose up</code> 来查看是否能够正常运行，以及是否能满足需求。</li><li>首先 <code>ctrl + c</code> 停止运行，再使用 <code>docker-compose up -d</code> 在后台运行。</li><li>如果需要修改配置，首先 <code>docker-compose down</code> 停下现有服务，修改完成后返回到第二步，重新检查并启动。</li><li>如果需要更新，运行 <code>docker-compose pull</code> 获取最新镜像，再 <code>docker-compose down</code> + <code>docker-compose up -d</code> 或是直接 <code>docker-compose restart</code> 来重启。</li></ol><h3>备份与还原</h3><p>我这里使用了一个 Shell 脚本来进行简单的备份。它的原理是把 Docker 需要的所有文件都打包成一个压缩文件，按照日期来命名，并通过 gpg 进行加密，最后放在另一个备份文件夹中。这个文件需要被放在 <code>docker</code> 目录下。</p><pre class="language-shell"><code>#!/bin/bash
tmp=$HOME/.tmp-backup
sudo rm -rf $tmp
mkdir $tmp
cd $HOME/docker

sudo tar -jcpf $tmp/rec-`/usr/bin/date "+%y-%m-%d"`.tar.bz2 .
sudo chown ubuntu:ubuntu $tmp/rec-`/usr/bin/date "+%y-%m-%d"`.tar.bz2
sudo mv -v $tmp/rec-`/usr/bin/date "+%y-%m-%d"`.tar.bz2 $HOME/test/
gpg -e -r pcrab -o $HOME/backup/rec-`/usr/bin/date "+%y-%m-%d"`.tar.bz2.gpg $tmp/rec-`/usr/bin/date "+%y-%m-%d"`.tar.bz2

sudo rm -rf $tmp
unset tmp</code></pre><p>如果需要在压缩时查看压缩了哪些文件，可以在 <code>tar</code> 的参数列表中加入 <code>-v</code>。</p><p>另外，我会将这一压缩包上传至阿里云的 <a href="https://www.aliyun.com/product/oss" target="_blank">OSS</a> 进行最后的备份。上传不消耗流量，如果需要恢复备份，由于我有一台阿里云的服务器，内网下载也不消耗流量，因此最后只需要购买存储容量包即可，用起来也非常方便。</p><p>如果需要定时自动备份，还可以通过 <code>crontab</code> 进行。执行 <code>crontab -e</code> 指令，修改配置文件即可。</p><pre class="language-null"><code># m h  dom mon dow   command
0 2 * * * /bin/bash /home/ubuntu/docker/backup.sh</code></pre><p>其中，最先的五个字符分别为 分钟，小时，日，月，星期。我这样配置就是每天凌晨两点运行脚本，自动进行备份。</p><p>如果需要还原，则可以通过 <code>sudo tar -jxpf filename.tar.bz2</code> 来解压缩。注意<strong>压缩与解压缩的时候，必须要通过 root 权限来进行操作，并加上 </strong><code><strong>-p</strong></code>，来保证权限与用户，用户组等属性的正确保留。</p><h3>清理</h3><p>在运行一段时间，经历过升级后，会发现服务器的储存空间被严重占用。出现这种情况很可能是 Docker 在运行期间产生的大量文件，以及更新后未被删除的旧镜像导致的，因此需要对其进行清理。</p><p>清理的方式非常简单。首先通过 <code>docker system df</code> 命令来查看具体的占用情况</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/b11f01761e87628ab4577de6db951ddf.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/b11f01761e87628ab4577de6db951ddf.png" referrerpolicy="no-referrer"><figcaption>这是已经清理过的，正常情况下 TOTAL 会远大于 ACTIVE</figcaption></figure><p>如果发现需要进行清理，那么可以通过 <code>docker system prune</code> 来进行清理。如果需要更彻底的清理，可以加上 <code>-a</code> 与 <code>--volumes</code> 参数。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/9e209d3befc2eb3beeb93ba44a0aa308.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/9e209d3befc2eb3beeb93ba44a0aa308.png" referrerpolicy="no-referrer"><figcaption>使用 -f 需要小心，注意防止误删除</figcaption></figure><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/da22a6035144a202fe2ae51cede9886c.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/da22a6035144a202fe2ae51cede9886c.png" referrerpolicy="no-referrer"><figcaption>可以发现每次尝试删除的提示都是不同的</figcaption></figure><p>另外，删除是需要一定时间来执行的，因此如果输入了 <code>y</code> 并会车后，中断看似卡死，实际上正在执行删除操作，需要耐心等待执行完毕。执行完成后会显示清理掉的内容以及清理了多少空间。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/647a527fcd60296d9546ccbf20b856b8.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/647a527fcd60296d9546ccbf20b856b8.png" referrerpolicy="no-referrer"></figure><h2>总结</h2><p>总体来说，使用 Docker Compose 来管理并没有想象中那么复杂。虽然需要一定的学习成本，但是具体使用起来就非常简单便捷了，只需找到对应的镜像，并按照说明进行配置即可，简单快捷。当然如果没有提供镜像，那么可能需要自己制作，这就需要更高的学习成本，可能比起直接在本机部署更加困难一些。</p><p>这里我也只是简单介绍了一下 Docker Compose 在服务器上部署的一些基础方式，也希望这篇文章能够给需要的人提供一些参考与帮助。</p><p> </p><p> </p></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-5179" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E9%80%9A%E8%BF%87%20Docker%20Compose%20%E7%AE%A1%E7%90%86%E6%88%91%E7%9A%84%E4%B8%AA%E4%BA%BA%E6%9C%8D%E5%8A%A1%E5%99%A8%E3%80%91%E6%88%91%E6%8B%A5%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%80%E5%8F%B0%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%8C%E4%B8%BB%E8%A6%81%E7%94%A8%E6%9D%A5%E9%83%A8%E7%BD%B2%E4%B8%80%E4%BA%9B%E6%88%91%E4%B8%AA%E4%BA%BA%E6%89%80%E9%9C%80%E8%A6%81%E7%9A%84%E6%9C%8D%E5%8A%A1%E3%80%82%E7%94%B1%E4%BA%8E%E4%BD%BF%E7%94%A8%E4%BA%86DockerCompose%EF%BC%8C%E7%9B%B8%E6%AF%94%E8%B5%B7%E7%9B%B4%E6%8E%A5%E9%83%A8%E7%BD%B2%EF%BC%8C%E6%9B%B4%E5%8A%A0%E4%BE%BF%E4%BA%8E%E7%AE%A1%E7%90%86%EF%BC%8C%E5%A4%87%E4%BB%BD%E7%AD%89%E3%80%82%E6%9C%AC%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F04%2F25%2Fcde3d20f45efb5f1070df7ac72d873b4.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-1573" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E9%80%9A%E8%BF%87%20Docker%20Compose%20%E7%AE%A1%E7%90%86%E6%88%91%E7%9A%84%E4%B8%AA%E4%BA%BA%E6%9C%8D%E5%8A%A1%E5%99%A8%E3%80%91%E6%88%91%E6%8B%A5%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84%E4%B8%80%E5%8F%B0%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%8C%E4%B8%BB%E8%A6%81%E7%94%A8%E6%9D%A5%E9%83%A8%E7%BD%B2%E4%B8%80%E4%BA%9B%E6%88%91%E4%B8%AA%E4%BA%BA%E6%89%80%E9%9C%80%E8%A6%81%E7%9A%84%E6%9C%8D%E5%8A%A1%E3%80%82%E7%94%B1%E4%BA%8E%E4%BD%BF%E7%94%A8%E4%BA%86DockerCompose%EF%BC%8C%E7%9B%B8%E6%AF%94%E8%B5%B7%E7%9B%B4%E6%8E%A5%E9%83%A8%E7%BD%B2%EF%BC%8C%E6%9B%B4%E5%8A%A0%E4%BE%BF%E4%BA%8E%E7%AE%A1%E7%90%86%EF%BC%8C%E5%A4%87%E4%BB%BD%E7%AD%89%E3%80%82%E6%9C%AC%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            