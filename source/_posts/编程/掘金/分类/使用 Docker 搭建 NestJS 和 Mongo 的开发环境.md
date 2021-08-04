
---
title: '使用 Docker 搭建 NestJS 和 Mongo 的开发环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6380'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 01:46:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=6380'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<p>本文介绍如何使用 <code>Docker</code> 搭建 <code>NestJS</code> 和 <code>MongoDB</code> 的开发环境。</p>
<p>完整项目地址： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLeoooY%2Fnest-mongo-docker-env" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LeoooY/nest-mongo-docker-env" ref="nofollow noopener noreferrer">github.com/LeoooY/nest…</a></p>
<p>要成功的将代码运行起来，并理解每个部分的工作原理，你至少需要对以下的知识点有基本的了解：</p>
<ul>
<li><code>JavaScript</code> & <code>TypeScript</code></li>
<li><code>Docker</code> 的基本使用</li>
<li><code>MongoDB</code> 的基本使用</li>
</ul>
<h2 data-id="heading-1">前置条件</h2>
<ul>
<li>安装 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.docker.com%2Fget-docker%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.docker.com/get-docker/" ref="nofollow noopener noreferrer"><code>Docker</code></a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.docker.com%2Fcompose%2Finstall%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.docker.com/compose/install/" ref="nofollow noopener noreferrer"><code>Docker-Compose</code></a></li>
<li>安装 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnodejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nodejs.org/" ref="nofollow noopener noreferrer"><code>NodeJS</code></a></li>
</ul>
<h2 data-id="heading-2">开始搭建</h2>
<p>主要步骤：</p>
<ol>
<li>创建 <code>NestJS</code> 项目</li>
<li>容器化 <code>NestJS</code> 项目</li>
<li>使用 <code>Docker-Compose</code> 编排容器</li>
<li>在 <code>NestJS</code> 项目中连接 <code>MongoDB</code> 服务</li>
</ol>
<h3 data-id="heading-3">创建 <code>NestJS</code> 项目</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.nestjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.nestjs.com/" ref="nofollow noopener noreferrer">Introduction | NestJS</a></p>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm i -g @nestjs/cli
$ nest new project-name
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <code>nest new</code> 命令创建完成后，<code>cd</code> 到 <code>project-name</code> 项目根目录执行 <code>start:dev</code>。</p>
<p>打开浏览器访问 <code>http://localhost:3000</code>，能正常访问就说明<code>NestJS</code> 项目已经创建好了。</p>
<h3 data-id="heading-4">容器化 <code>NestJS</code> 项目</h3>
<p>在这个步骤，我们需要刚刚创建的<code>NestJS</code> 项目打包成一个 <code>Docker</code> 容器。</p>
<ol>
<li>首先在 <code>NestJS</code> 项目根目录新建一个 <code>Dockerfile</code> 文件</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ touch Dockerfile
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改 <code>Dockerfile</code> 文件内容</li>
</ol>
<pre><code class="copyable">
# Docker多阶段构建

### DEV环境 ###
FROM node:14.17.3 AS development

# 定位到容器工作目录
WORKDIR /usr/src/app
# 拷贝package.json
COPY package*.json ./

RUN npm install glob rimraf
RUN npm install --only=development
COPY . .
RUN npm run build


### PROD环境 ###
FROM node:14.17.3 as production

ARG NODE_ENV=production
ENV NODE_ENV=$&#123;NODE_ENV&#125;

WORKDIR /usr/src/app

COPY package*.json ./

RUN \
  npm config set registry https://registry.npm.taobao.org \
  && npm install --only=production

COPY . .

COPY --from=development /usr/src/app/dist ./dist

CMD ["node", "dist/main"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一个 <code>NestJS</code> 项目的 <code>Docker</code> 镜像就定制好了。</p>
<blockquote>
<p>由于还有 <code>MongoDB</code> 相关的容器服务，我们不直接使用 <code>Docker</code> 命令来构建、运行，而是使用 <code>Docker-Compose</code> 编排容器</p>
</blockquote>
<h3 data-id="heading-5">使用 <code>Docker-Compose</code> 编排容器</h3>
<p><code>Docker-Compose</code> 的 <code>docker-compose.yml</code> 配置文件可以将一组相关联的应用容器定义为一个项目，这样我们可以很方便的管理 <code>NestJS</code> 和 <code>MongoDB</code> 的服务。</p>
<ol>
<li>在 <code>NestJS</code> 项目根目录新建一个 <code>docker-compose.yml</code> 文件</li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ touch docker-compose.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>修改 <code>docker-compose.yml</code> 文件内容</li>
</ol>
<pre><code class="copyable">version: '3.9'
services:
  dev:
    container_name: server-dev
    image: server-dev:1.0.0
    build:
      context: .
      target: development
      dockerfile: ./Dockerfile
    command: npm run start:debug
    ports:
      - 3000:3000
      - 9229:9229
    networks:
      - server-network
    volumes:
      - .:/usr/src/app
      - /usr/src/app/node_modules
    restart: unless-stopped
    environment:
      MONGO_URL: mongodb
  prod:
    container_name: server-prod
    image: server-prod:1.0.0
    build:
      context: .
      target: production
      dockerfile: ./Dockerfile
    command: npm run start:prod
    ports:
      - 3000:3000
      - 9229:9229
    networks:
      - server-network
    volumes:
      - .:/usr/src/app
      - /usr/src/app/node_modules
    restart: unless-stopped
  mongodb:
    image: mongo:5.0.0
    container_name: server-mongodb
    environment:
      - MONGO_INITDB_ROOT_USERNAME=root
      - MONGO_INITDB_ROOT_PASSWORD=pass12345
    volumes:
      - mongodb-data:/data/db
    networks:
      - server-network
    ports:
      - 27017:27017
    healthcheck:
      test: echo 'db.runCommand("ping").ok' | mongo localhost:27017/test --quiet
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
  mongo-express:
    image: mongo-express
    container_name: server-mongo-express
    environment:
      - ME_CONFIG_MONGODB_SERVER=mongodb
      - ME_CONFIG_MONGODB_ENABLE_ADMIN=true
      - ME_CONFIG_MONGODB_ADMINUSERNAME=root
      - ME_CONFIG_MONGODB_ADMINPASSWORD=pass12345
      - ME_CONFIG_BASICAUTH_USERNAME=admin
      - ME_CONFIG_BASICAUTH_PASSWORD=admin123
    volumes:
      - mongodb-data
    depends_on:
      - mongodb
    networks:
      - server-network
    ports:
      - 8081:8081
    healthcheck:
      test: wget --quiet --tries=3 --spider http://admin:admin123@localhost:8081 || exit 1
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped
volumes:
  mongodb-data:
    name: mongodb-data
networks:
  server-network:
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这一步，我们已经完成了容器化的所有步骤，剩下的就是在 <code>NestJS</code> 去连接 <code>MongoDB</code> 服务。</p>
<h3 data-id="heading-6">在 <code>NestJS</code> 项目中连接 <code>MongoDB</code> 服务</h3>
<p>我们使用 <code>NestJS</code> 推荐的 <code>@nestjs/mongoose</code> 工具来连接 <code>MongoDB</code> 服务。</p>
<ol>
<li>安装 <code>@nestjs/mongoose</code></li>
</ol>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install --save @nestjs/mongoose mongoose 
<span class="hljs-comment"># or yarn</span>
$ yarn add -D @nestjs/mongoose mongoose 
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>连接 <code>MongoDB</code> 服务</li>
</ol>
<p><code>app.module.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Module &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@nestjs/common'</span>;
<span class="hljs-keyword">import</span> &#123; AppController &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./app.controller'</span>;
<span class="hljs-keyword">import</span> &#123; AppService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./app.service'</span>;
<span class="hljs-keyword">import</span> &#123; MongooseModule &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@nestjs/mongoose'</span>;

<span class="hljs-keyword">const</span> url = process.env.MONGO_URL || <span class="hljs-string">'localhost'</span>;

<span class="hljs-meta">@Module</span>(&#123;
  <span class="hljs-attr">controllers</span>: [AppController],
  <span class="hljs-attr">providers</span>: [AppService],
  <span class="hljs-attr">imports</span>: [
    MongooseModule.forRoot(
      <span class="hljs-string">`mongodb://<span class="hljs-subst">$&#123;url&#125;</span>:27017?serverSelectionTimeoutMS=2000&authSource=admin`</span>,
    ),
  ],
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppModule</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意的是我们使用的 <code>mongodb</code> 连接地址 <code>process.env.MONGO_URL</code> 是 <code>docker-compose.yml</code> 中定义的 <code>mongodb</code> 服务的地址，参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F42385977%2Faccessing-a-docker-container-from-another-container" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/42385977/accessing-a-docker-container-from-another-container" ref="nofollow noopener noreferrer">Accessing a docker container from another container。</a></p>
</blockquote>
<h2 data-id="heading-7">启动项目</h2>
<p>现在，我们已经完成了所有的配置工作，可以把项目给跑起来了。</p>
<p>启动 <code>NestJS</code> 服务、<code>Mongo</code> 服务和 <code>Mongo-Express</code> 服务。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ docker-compose up -d dev mongodb mongo-express
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：当你使用 <code>npm</code> 安装了新的 <code>package</code> 时，需要使用 <code>-V</code> 参数来重新创建容器的 <code>node_modules</code> 匿名数据卷。</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">$ docker-compose up -d -V dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看各个容器的状态</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ docker ps 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>查看容器的日志</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ docker logs server-dev 
$ docker logs server-dev -f <span class="hljs-comment"># -f 用于参数持续输出logs</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入容器 <code>shell</code></p>
<pre><code class="hljs language-bash copyable" lang="bash">$ docker <span class="hljs-built_in">exec</span> -it server-mongodb bash <span class="hljs-comment"># 进入mongo容器</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdev.to%2Ferezhod%2Fsetting-up-a-nestjs-project-with-docker-for-back-end-development-30lg" target="_blank" rel="nofollow noopener noreferrer" title="https://dev.to/erezhod/setting-up-a-nestjs-project-with-docker-for-back-end-development-30lg" ref="nofollow noopener noreferrer">Setting up a NestJS project with Docker for Back-End development</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fcontainerized-development-nestjs-docker%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/containerized-development-nestjs-docker/" ref="nofollow noopener noreferrer">Containerized development with NestJS and Docker</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bmc.com%2Fblogs%2Fmongodb-docker-container%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bmc.com/blogs/mongodb-docker-container/" ref="nofollow noopener noreferrer">How To Run MongoDB as a Docker Container</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.programmersought.com%2Farticle%2F16254481182%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.programmersought.com/article/16254481182/" ref="nofollow noopener noreferrer">Containerize Nest.js+MongoDB application in 5 minutes</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F42385977%2Faccessing-a-docker-container-from-another-container" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/42385977/accessing-a-docker-container-from-another-container" ref="nofollow noopener noreferrer">Accessing a docker container from another container</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F24319662%2Ffrom-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/24319662/from-inside-of-a-docker-container-how-do-i-connect-to-the-localhost-of-the-mach" ref="nofollow noopener noreferrer">From inside of a Docker container, how do I connect to the localhost of the machine?</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyeasy.gitbook.io%2Fdocker_practice%2Fcompose%2Fcompose_file" target="_blank" rel="nofollow noopener noreferrer" title="https://yeasy.gitbook.io/docker_practice/compose/compose_file" ref="nofollow noopener noreferrer">Docker从入门到实践</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Feggjs%2Fdocker%2Fblob%2Fmaster%2FDockerfile" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/eggjs/docker/blob/master/Dockerfile" ref="nofollow noopener noreferrer">Eggjs Dockerfile</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnestjs%2Fmongoose" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nestjs/mongoose" ref="nofollow noopener noreferrer"><code>@nestjs/mongoose</code></a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fa%2F32785014%2F12395601" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/a/32785014/12395601" ref="nofollow noopener noreferrer">Docker-compose: node_modules not present in a volume after npm install succeeds</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.docker.com%2Fblog%2Fkeep-nodejs-rockin-in-docker%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.docker.com/blog/keep-nodejs-rockin-in-docker/" ref="nofollow noopener noreferrer">Top 4 Tactics To Keep Node.js Rockin’ in Docker</a></li>
</ul></div>  
</div>
            