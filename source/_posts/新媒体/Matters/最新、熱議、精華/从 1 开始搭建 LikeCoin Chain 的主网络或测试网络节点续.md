
---
title: '从 1 开始搭建 LikeCoin Chain 的主网络或测试网络节点续'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/d9ef6eb2-e0ab-4645-bb9e-96c4f043bda2.png'
author: Matters
comments: false
date: Tue, 11 Jan 2022 15:14:57 GMT
thumbnail: 'https://assets.matters.news/embed/d9ef6eb2-e0ab-4645-bb9e-96c4f043bda2.png'
---

<div>   
<h2><strong>连接到虚拟机</strong></h2><p>虽然 DigitalOcean 和 Linode 都能通过网页连接来着。</p><p>DigitalOcean 是在 Droplet 的 Console 那里。</p><figure class="image"><img src="https://assets.matters.news/embed/d9ef6eb2-e0ab-4645-bb9e-96c4f043bda2.png" data-asset-id="d9ef6eb2-e0ab-4645-bb9e-96c4f043bda2" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>打开的效果大概是这样。</p><figure class="image"></figure><figure class="image"><img src="https://assets.matters.news/embed/ecbc0559-efe6-4d40-9c50-14a53418cab3.png" data-asset-id="ecbc0559-efe6-4d40-9c50-14a53418cab3" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>Linode 是在 Linode 详情那里，有个 “Launch LISH Console” 的按钮，在 Reboot 的旁边。</p><figure class="image"><img src="https://assets.matters.news/embed/d10deb7e-2a68-4196-b115-dc7a6e28a8e8.png" data-asset-id="d10deb7e-2a68-4196-b115-dc7a6e28a8e8" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>打开大概像这样。 </p><blockquote>不过按照 <a href="https://www.linode.com/docs/guides/using-the-lish-console/" rel="noopener noreferrer" target="_blank">Linode 的文档</a>，Lish 差不多算是个虚拟终端，于是即使因为配置不正确或者其他原因导致后面提起的 SSH 登录不上的时候， Lish 应该也可以用。</blockquote><figure class="image"><img src="https://assets.matters.news/embed/85d081c0-1249-4763-8d52-cf3b108b7375.png" data-asset-id="85d081c0-1249-4763-8d52-cf3b108b7375" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>不过咱更习惯用本地的 SSH 客户端来连接就是了。如果汝觉得网页连接也 OK 的话，可以跳过下面 SSH 连接的部分。</p><h2><strong>所以 SSH 是什么？</strong></h2><blockquote>Secure Shell（縮寫为SSH），由IETF的網路工作小組（Network Working Group）所制定；SSH為一项建立在应用层和传输层基础上的安全协议，为计算机上的Shell（壳层）提供安全的传输和使用环境。</blockquote><blockquote>而SSH是目前较可靠，專为远程登录会话和其他网络服务提供安全性的协议。利用SSH协议可以有效防止远程管理过程中的信息泄露问题。透過SSH可以對所有传输的数据进行加密，也能够防止DNS欺骗和IP欺骗。</blockquote><blockquote>SSH之另一項優點為其传输的数据可以是经过压缩的，所以可以加快传输的速度。SSH有很多功能，它既可以代替Telnet，又可以为FTP、POP、甚至为PPP提供一个安全的「通道」。</blockquote><p>或者一个在当下更简单的说法，就是一个相对安全的连接方法了。</p><h2><strong>准备一个 SSH 客户端</strong></h2><blockquote>其实是终端应用加上 OpenSSH 客户端啦，这里就先不解释具体是什么了，想要进一步了解的话也可以自己搜索一下。</blockquote><ul><li>Mac 的话，自带的终端 App 就可以了。</li></ul><figure class="image"><img src="https://assets.matters.news/embed/3cbcbfda-22ea-4de4-9dc4-29849d9f58e8.png" data-asset-id="3cbcbfda-22ea-4de4-9dc4-29849d9f58e8" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><ul><li>Windows 的话，<a href="https://docs.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse#install-openssh-using-powershell" rel="noopener noreferrer" target="_blank">可以参考 Microsoft 的文档</a> 安装 OpenSSH，推荐搭配 <a href="https://docs.microsoft.com/zh-cn/windows/terminal/install" rel="noopener noreferrer" target="_blank">Windows Terminal</a> 使用。</li></ul><figure class="image"><img src="https://assets.matters.news/embed/8a188639-fd96-4de3-96ce-5cadde1f60d3.png" data-asset-id="8a188639-fd96-4de3-96ce-5cadde1f60d3" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>下面就都以终端代称了。</p><h2><strong>连接</strong></h2><p>首先从管理面板那里吧汝的虚拟机的 IP 地址复制下来，然后打开终端，输入下面这一行：</p><blockquote>ssh root@这里是汝复制下来的IP地址</blockquote><p>当汝按下 Enter 键确认以后，应该会是这个样子：</p><pre class="ql-syntax" spellcheck="false">The authenticity of host 'localhost (::1)' can't be established.
ECDSA key fingerprint is SHA256:ZrEikKJj6wqLk8Cqgs6JWXGX3FgS2iQI6aK73GTCHVk.
Are you sure you want to continue connecting (yes/no)?
</pre><p>大概的意思就是“咱好像不记得汝要去的这个地方呐~”，毕竟是第一次连接嘛。</p><p>如果确认了以后，就输入 yes 让 ssh 客户端记下来。</p><p>然后：</p><pre class="ql-syntax" spellcheck="false">Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.
root@localhost's password:
</pre><p>这里输入密码。记得输入密码时就是什么都没有，不用担心键盘坏了啦~</p><pre class="ql-syntax" spellcheck="false">Last login: Tue Jan 11 21:30:45 2022
root@debian-s-1vcpu-2gb-intel-sgp1-01:~#
</pre><p>如果在 DigitalOcean 的虚拟机上附加了存储并且选择了自动配置的话，可以用 <code>lsblk</code> 命令看看它挂载到了那里。</p><pre class="ql-syntax" spellcheck="false">root@debian-s-1vcpu-2gb-intel-sgp1-01:~# lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda   8:0 0 100G 0 disk /mnt/volume_sgp1_02
vda  254:0 0 50G 0 disk 
├─vda1 254:1 0 49.9G 0 part /
├─vda14 254:14 0 3M 0 part 
└─vda15 254:15 0 124M 0 part /boot/efi
vdb  254:16 0 474K 1 disk 
</pre><p>在这个例子里就是那个 /mnt/volume_sgp1_02 了。</p><h2><strong>安装 Docker 和 docker-compose</strong></h2><blockquote>如果汝不是和咱一样用的 Debian 11 的话，可以去 <a href="https://docs.docker.com/engine/install/" rel="noopener noreferrer" target="_blank">Docker 自己的文档</a>上查阅适用于自己的发行版的安装方法。</blockquote><ul><li>安装基础的组件。</li></ul><pre class="ql-syntax" spellcheck="false">$ sudo apt-get update
​
$ sudo apt-get install \
 ca-certificates \
 curl \
 gnupg \
 lsb-release
</pre><ul><li>添加 Docker 存储库的 GnuPG 公钥。</li></ul><pre class="ql-syntax" spellcheck="false">$ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
</pre><ul><li>添加 Docker 存储库。</li></ul><pre class="ql-syntax" spellcheck="false">$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
 $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
</pre><ul><li>安装 Docker。</li></ul><pre class="ql-syntax" spellcheck="false"> $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io
</pre><ul><li>可以运行一下 Docker 官方的 Hello World 映像来确认是否运行正常。</li></ul><pre class="ql-syntax" spellcheck="false"> sudo docker run hello-world
</pre><ul><li>接下来下载 docker-compose。</li></ul><pre class="ql-syntax" spellcheck="false">$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
</pre><ul><li>因为在 Debian 这样的 GNU/Linux 发行版上是依靠文件是否具有可执行权限来决定一个文件是否能执行的，所以需要可执行权限。</li></ul><pre class="ql-syntax" spellcheck="false">$ sudo chmod +x /usr/local/bin/docker-compose
</pre><ul><li>运行一下，应该会输出 docker-compose 的帮助信息。</li></ul><pre class="ql-syntax" spellcheck="false">$ docker-compose
​
Usage: docker compose [OPTIONS] COMMAND
​
Docker Compose
​
……
​
Run 'docker compose COMMAND --help' for more information on a command.
</pre><h2><strong>新建一个用户</strong></h2><p>因为 root 用户的权力很大而且很危险，所以轻易不会用到它。通常都是用一个普通用户进行日常操作，在需要的时候再通过 sudo  这样的命令来切换。</p><p>下面这条命令可以新建一个用户，并让它加入到 sudo 组里允许它使用 sudo 命令。</p><blockquote>就像是约定俗成的一样，大家都习惯在文档里用 # 开头表示需要 root 用户运行的命令，用 $ 表示普通用户可以运行的命令，所以复制下面的指令的时候不用把最前面的 # 或者 $ 符号复制进去。</blockquote><pre class="ql-syntax" spellcheck="false"># useradd -u 1000 -m -s /bin/bash -G sudo,docker 这里是汝想要的用户名
</pre><p>然后设置一个密码。</p><pre class="ql-syntax" spellcheck="false"># passwd 这里是汝刚刚输入的用户名
</pre><h2><strong>准备运行主网络节点</strong></h2><p>安装 Git，一会儿要用它来下载需要的文件。</p><pre class="ql-syntax" spellcheck="false">$ sudo apt install git
</pre><p>下载 LikeCoin Chain 的代码。</p><pre class="ql-syntax" spellcheck="false">$ git clone https://github.com/likecoin/likecoin-chain --branch fotan-1.1 --single-branch && cd likecoin-chain
</pre><p>复制一份 docker-compose 使用的模板文件和环境变量文件。</p><pre class="ql-syntax" spellcheck="false">$ cp docker-compose.yml.template docker-compose.yml
$ cp .env.template .env
</pre><p>编辑 .env 文件，这里的命令用的是相对简单一些的 nano。<a href="https://www.nano-editor.org/dist/latest/nano.html" rel="noopener noreferrer" target="_blank">文档在这里</a>。以及 nano 下面也有一些基本的操作提示来着。</p><figure class="image"><img src="https://assets.matters.news/embed/b1fd3a97-d014-4948-acfb-98af58bc7ce1.png" data-asset-id="b1fd3a97-d014-4948-acfb-98af58bc7ce1" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>下面给出一个文件作为参考吧。</p><pre class="ql-syntax" spellcheck="false"># Basic configs
# 以 # 开头的一行是给人类看的注释，程序运行时并不在意这些。
# 使用的 Docker 映像，保持默认的就好。
LIKECOIN_DOCKER_IMAGE="likecoin/likecoin-chain:fotan-1.1"
# 最小单位币种的单位和链的名称。
# 如果汝要运行主网络节点的话是这两行。
LIKECOIN_TOKEN_DENOM="nanolike"
LIKECOIN_CHAIN_ID="likecoin-mainnet-2"
# 如果是测试网络的话就是这两行。EKIL 就是反过来的 LIKE 啦。
LIKECOIN_TOKEN_DENOM="nanoekil"
LIKECOIN_CHAIN_ID="likecoin-public-testnet-3"
​
# 运行 Docker 容器的用户。如果汝是用刚才的 useradd 新建的用户的话，这一行应该不用修改。
# 如果汝知晓以 root 用户运行的风险的话，也可以把这里修改成 0 。
LIKECOIN_UID="1000"
​
# 节点自动关闭的时间或者区块高度。这个在升级时会用到，所以面前不需要修改。
LIKECOIN_HALT_TIME="0"
LIKECOIN_HALT_HEIGHT="0"
​
# 节点的名称，取个自己喜欢的就好
LIKECOIN_MONIKER="Foo"
​
# 创世文件的地址，上面一行是主网络的，下面一行是测试网络的。
LIKECOIN_GENESIS_URL="https://gist.githubusercontent.com/williamchong/de1bdf2b2a8f3bce50a4b5e46af26959/raw/4e21bff586771c849d22e1916bcb88c6463fbaa0/genesis.json"
LIKECOIN_SEED_NODES="913bd0f4bea4ef512ffba39ab90eae84c1420862@34.82.131.35:26656,e44a2165ac573f84151671b092aa4936ac305e2a@nnkken.dev:26656"
​
# LIKECOIN_SEED_NODES is for bootstraping the network. These are the entry point of the node to the network.
# Format: "ID@IP_OR_DOMAIN:PORT", where `ID` is a hexadecimal string.
# May fill in multiple seed nodes by separating them in comma (",").
# 起始的种子节点，汝的节点会先从它们那里获得其它节点的信息。
# 上面一行是主网络的，下面一行是测试网络的。
LIKECOIN_SEED_NODES="913bd0f4bea4ef512ffba39ab90eae84c1420862@34.82.131.35:26656,e44a2165ac573f84151671b092aa4936ac305e2a@nnkken.dev:26656"
LIKECOIN_SEED_NODES="c5e678f14219c1f161cb608aaeda37933d71695d@nnkken.dev:31801"
​
# Consensus public key of the node, used for creating validator.
# This variable should be set automatically during the init script.
# Could also be obtained by running `docker-compose run --rm liked-command tendermint show-validator`.
# 节点的公钥，这个会在下面的命令中自动填入，所以不需要修改。
LIKECOIN_VALIDATOR_PUBKEY=""
</pre><p>初始化需要的 .liked 目录：</p><pre class="ql-syntax" spellcheck="false">$ docker-compose run --rm init
Initialized ./.liked folder as node data folder.
Validator public key (cosmosvalconspub1zcjduepqjsxy2m95a0p0vf66gmuar68dztscmgt47p8r0n4g80qq9zpwvexsus9f5h) has been written into .env file.
​
The genesis path is a URL, downloading.
curl found, downloading using curl.
​
Genesis file installed into .liked/config folder.
Please verify with the SHA256 checksum:
dbca3908f6dc154abab61bd6ae25459e2ae74733fb91cc1d4f1cdcdffd16c69f /host/.liked/config/genesis.json
</pre><p>要确认下载的创世文件是否正确的话，把下面命令的输出和最后一行对比一下。</p><pre class="ql-syntax" spellcheck="false">$ sha256sum .liked/config/genesis.json
dbca3908f6dc154abab61bd6ae25459e2ae74733fb91cc1d4f1cdcdffd16c69f .liked/config/genesis.json
</pre><p>创建钱包，这里会要求输入两次保护私钥的密码：</p><pre class="ql-syntax" spellcheck="false">$ docker-compose run --rm liked-command keys add validator
</pre><p>其实最后的 vaildator 是钱包的名称啦。所以这是有机会创建好几个钱包么？</p><pre class="ql-syntax" spellcheck="false">Enter keyring passphrase:
Re-enter keyring passphrase:
​
- name: validator
 type: local
 address: cosmos1668dckejgjv63zj57zju65lufzuuhzue3hnrfd
 pubkey: cosmospub1addwnpepqw2rq99wt9xjhlcre9g4uuayur2s5d8zu6wakxdwxfa0d23u4djxj7zcxuj
 mnemonic: ""
 threshold: 0
 pubkeys: []
​
​
**Important** write this mnemonic phrase in a safe place.
It is the only way to recover your account if you ever forget your password.
giggly sludge posing culture domain playmaker afternoon probe surfer subscript aptitude rename scale uncut parasitic basics railroad glacial gerbil eternal
</pre><h2><strong>⚠️ 当然了，这个只是拿来示范用的，汝自己要记得把下面的助记词复制下来，不要告诉任何人！</strong></h2><h2><strong>⚠️ 当然了，这个只是拿来示范用的，汝自己要记得把下面的助记词复制下来，不要告诉任何人！</strong></h2><h2><strong>⚠️ 当然了，这个只是拿来示范用的，汝自己要记得把下面的助记词复制下来，不要告诉任何人！</strong></h2><p>（重要的话要讲三遍，笑）</p><p>启动节点，如果不加最后的 -d 的话，运行时的日志会输出在屏幕上，需要调试的时候也许有用。</p><pre class="ql-syntax" spellcheck="false">$ docker-compose up -d
</pre><p>可以查看日志观察有没有错误。--tails 后面的数字表示显示最新的多少行。</p><pre class="ql-syntax" spellcheck="false">$ docker-compose logs --tails=10
</pre><p>或者也可以通过节点提供的 API 查看状态。</p><pre class="ql-syntax" spellcheck="false">$ curl http://localhost:26657/status
&#123;
 "jsonrpc": "2.0",
 "id": -1,
 "result": &#123;
 "node_info": &#123;
  "protocol_version": &#123;
   "p2p": "8",
   "block": "11",
   "app": "0"
  &#125;,
  "id": "664e541b7e64a9aa1aded168e40fb7b4c16fca1c",
  "listen_addr": "tcp://172.105.148.120:26656",
  "network": "likecoin-public-testnet-3",
  "version": "0.34.11",
  "channels": "40202122233038606100",
  "moniker": "Horo.Dev",
  "other": &#123;
   "tx_index": "on",
   "rpc_address": "tcp://0.0.0.0:26657"
  &#125;
 &#125;,
 "sync_info": &#123;
  "latest_block_hash": "F1735207215EDD0CE7AA60FB7A4A206E462B29A975098AA13CFBD09A637EA0E6",
  "latest_app_hash": "BB76B980D8D56458AD2EBF152FD702FADD16EEDCDCC191975A87AB3D9A999EA0",
  "latest_block_height": "2546072",
  "latest_block_time": "2022-01-11T15:05:23.309549125Z",
  "earliest_block_hash": "E16B701D9C9C017AF7A3A07CA752CB5B06A48D17163E0C3C5C32F122A8F1315E",
  "earliest_app_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
  "earliest_block_height": "1",
  "earliest_block_time": "2021-07-28T13:30:00Z",
  "catching_up": false
 &#125;,
 "validator_info": &#123;
  "address": "ADDF562A12F61C7C955364224A9675FB1F847072",
  "pub_key": &#123;
   "type": "tendermint/PubKeyEd25519",
   "value": "arB/RtcGcdIG5GJhD1MjSC7fjDSzmnErjZochUrkhXE="
  &#125;,
  "voting_power": "0"
 &#125;
 &#125;
&#125;
</pre><p>当 sync_info 里的 catching_up 显示为 false 的时候，代表汝的节点的状态是最新的了，</p><hr><p>那么接下来就等待节点同步上最新的数据吧。</p>  
</div>
            