
---
title: '部署Iron Fish测试网节点'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/2c070ee6-6e67-414a-b180-5d8a6ef84b90.png'
author: Matters
comments: false
date: Thu, 02 Dec 2021 04:54:46 GMT
thumbnail: 'https://assets.matters.news/embed/2c070ee6-6e67-414a-b180-5d8a6ef84b90.png'
---

<div>   
<p>最近测试网的任务真多，一个接一个。这个Iron Fish之前测试网也很久了，但是今天的这个测试网是有奖励的。</p><p>机制和Aleo差不多，挖到一块获得100积分。上主网后，估计按照积分比例分配主网币</p><p>Iron Fish有奖励的测试网介绍：<a href="https://ironfish.network/blog/2021/11/30/series-a-incentivized-testnet" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://ironfish.network/blog/2021/11/30/series-a-incentivized-testnet</a></p><figure class="image"><img src="https://assets.matters.news/embed/2c070ee6-6e67-414a-b180-5d8a6ef84b90.png" data-asset-id="2c070ee6-6e67-414a-b180-5d8a6ef84b90" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>Iron Fish的节点部署：<a href="https://ironfish.network/docs/onboarding/iron-fish-tutorial" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://ironfish.network/docs/onboarding/iron-fish-tutorial</a></p><h3>最低配置</h3><p>官方没有给出最低配置，但是看起来需要不少CPU。CPU越好，挖的越快</p><h3>安装Docker</h3><pre class="ql-syntax" spellcheck="false">sudo apt update
sudo apt upgrade
apt install docker.io
</pre><h3>启动容器</h3><pre class="ql-syntax" spellcheck="false">docker run -d --name=ironfish --network host --volume /data/ironfish/.ironfish:/root/.ironfish ghcr.io/iron-fish/ironfish:latest
</pre><h3>进入容器</h3><pre class="ql-syntax" spellcheck="false">docker exec -it ironfish bash
</pre><h3>创建账号</h3><p>进入容器后，输入下面的命令：</p><pre class="ql-syntax" spellcheck="false">ironfish accounts:create
</pre><figure class="image"><img src="https://assets.matters.news/embed/c6328c46-24c4-45c0-80a8-6072ac228048.png" data-asset-id="c6328c46-24c4-45c0-80a8-6072ac228048" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>创建成功后，输入下面的命令设置默认的账号:</p><pre class="ql-syntax" spellcheck="false">ironfish accounts:use MyNewAccount
</pre><h3>领取测试币</h3><pre class="ql-syntax" spellcheck="false">ironfish faucet
</pre><h3>配置Graffiti</h3><p>这个后面排行榜注册需要</p><pre class="ql-syntax" spellcheck="false">ironfish config:set blockGraffiti "xxxxx"
</pre><p>*xxxxx 任意名字</p><h3>开启后台挖矿程序</h3><pre class="ql-syntax" spellcheck="false">nohup ironfish miners:start &>/tmp/ironfish.log &
</pre><p>好了，挖矿程序就顺利运行了</p><h3>进入容器后的一些命令</h3><h6>#查看程序状态</h6><p><code>ironfish status -f</code></p><h6>#查看代币余额</h6><p><code>ironfish accounts:balance</code></p><h6>#查看当前账户</h6><p><code>ironfish accounts:which</code></p><h5>#查看当前账户公共地址</h5><p><code>ironfish accounts:publickey</code></p><h5>#代币转账</h5><p><code>ironfish accounts:pay</code></p><h3>升级版本</h3><p>测试网问题是比较多，所以升级也很频繁。如果要升级，按照下面的步骤:</p><h5># 下载最新的容器：</h5><p><code>docker pull ghcr.io/iron-fish/ironfish:latest</code></p><h5># 重设数据：</h5><p><code>docker run --rm --tty --interactive --network host --volume $HOME/.ironfish:/root/.ironfish ghcr.io/iron-fish/ironfish:latest reset</code></p><h5># 启动新的容器：</h5><pre class="ql-syntax" spellcheck="false">docker run -d --name=ironfish --network host --volume /data/ironfish/.ironfish:/root/.ironfish ghcr.io/iron-fish/ironfish:latest
</pre><h3>注册并查看测试网积分</h3><p>网站：<a href="https://testnet.ironfish.network/leaderboard" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://testnet.ironfish.network/leaderboard</a></p><p>点击"Sign Up"</p><figure class="image"><img src="https://assets.matters.news/embed/1e046356-5501-4bd6-ae08-4ce8fa1c6a66.png" data-asset-id="1e046356-5501-4bd6-ae08-4ce8fa1c6a66" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>输入邮箱，Graffiti(上面设置的Graffiti名), Discord ID 和国家</p><figure class="image"><img src="https://assets.matters.news/embed/061af0c5-85f3-4803-b559-6c410638f856.png" data-asset-id="061af0c5-85f3-4803-b559-6c410638f856" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>注册成功后，你就可以在leaderboard上查看你的挖矿成果了</p><figure class="image"><img src="https://assets.matters.news/embed/1e2ead42-b3a0-4d5f-9a02-c82f6d2b13bd.png" data-asset-id="1e2ead42-b3a0-4d5f-9a02-c82f6d2b13bd" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p>  
</div>
            