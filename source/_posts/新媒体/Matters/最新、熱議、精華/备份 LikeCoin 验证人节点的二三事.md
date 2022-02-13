
---
title: '备份 LikeCoin 验证人节点的二三事'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/2f787a49-4c5e-4d6c-a560-c4f6e4914f12.png'
author: Matters
comments: false
date: Sat, 12 Feb 2022 17:27:59 GMT
thumbnail: 'https://assets.matters.news/embed/2f787a49-4c5e-4d6c-a560-c4f6e4914f12.png'
---

<div>   
<h2>从一块墓碑开始（什么意思）</h2><p>最近几天在 Discord 聊天的时候看到有位验证人（<a href="https://likecoin.bigdipper.live/validators/cosmosvaloper1xnpa0k9ywwmk3lmysxred94zamffwkqmna5wur" rel="noopener noreferrer" target="_blank">BusinessAsMission</a> 啦）在迁移验证人节点的时候出了一些意外不得不另起炉灶重新建立验证人节点的样子（步 <a class="mention" href="https://matters.news/@thumbb13555" target="_blank" data-display-name="碼農日常" data-user-name="thumbb13555" data-id="VXNlcjo1NzI3NA">﻿<span>@碼農日常</span>﻿</a>  后尘是吧，笑）。虽然这次的事故更大就是了。</p><p>简单来说呢，就是 BusinessAsMission 之前发现验证人节点的存储有一些问题以后，就打算迁移到新的服务器上。但是过程中他们好像忘记先把旧的节点停下来了，于是可能在某个时间点因为新旧两个节点都在线还签了名，犯了双重签名大忌被打成墓碑了的样子。</p><figure class="image"><img src="https://assets.matters.news/embed/2f787a49-4c5e-4d6c-a560-c4f6e4914f12.png" data-asset-id="2f787a49-4c5e-4d6c-a560-c4f6e4914f12" referrerpolicy="no-referrer"><figcaption><span>（于是就有了 LikeCoin Chain 第一个 Tombstoned 的验证人节点）</span></figcaption></figure><h2>一点题外话 – 什么会导致委托人的委托被削减？</h2><p>从某种角度来说，对验证人的委托就相当于 Likers 在技术力、知识或诚信，以及其他方面信任那位验证人，并以委托的那部分 LikeCoin 的流动性为代价同意让她代表自己参与社群治理（就是投票权啦），以及和验证人分享验证交易的回报。</p><p>不过哪里差不多赏罚分明，如果验证人不能履行责任或者涉嫌恶意操作，也是会受到处罚的。处罚之一就是委托的 LikeCoin 会按照一定比例扣减（就是上面的削减啦）。因为这个削减也会同时影响到委托给她的 Likers ，于是对 Likers 来说，虽然已经强调很多次了，委托不能只看佣金率，还要确保汝足够信任和支持汝要委托给的那位验证人才行。</p><p>于是，委托会被削减的原因有两种：</p><ul><li>因为不在线而入狱（Jailed），如果某位验证人在指定的区间内签署的区块数量过少（LikeCoin Chain 的设定是每 10000 块中小于 500 块，以目前平均 6 秒产生一个区块来计算的话，大概是连续不在线 15 个小时），验证人的状态就会转为 Jailed （也就是所谓的坐牢啦）。被委托的 LikeCoin 中的 0.01% 会被削减，而验证人可以在 Jailed 至少十分钟后自行“出狱”回到入狱前的状态。</li><li>因为双重签署而永久解职（Tombstoned，墓碑化么……），如果某位验证人同时签署两项冲突的交易。因为这会导致一笔款项可能被重复使用多次，所以算得上是严重错误了。犯此错误的验证人会被永久解除职务，而被委托的 LikeCoin 中的 5% 会被削减。</li></ul><p>所以呢……因为双重签署的严重性比不在线严重的多得多的多，所以从中能得到的教训就是：如果要进行像是备份或迁移之类的操作，一定不要忘了先把原有的节点停下来。毕竟坐牢还可以出狱，成了墓碑就不好挽回了，是吧。</p><h2>于是要备份验证人节点的话，最关键的是什么？</h2><blockquote>终于开始正题了 😂</blockquote><p>最关键的就是私钥啦，和汝用的其它钱包差不多。毕竟区块的数据如果没了也许其它节点那里还可以拿，但是私钥丢了嘛……那谁也救不了了。</p><p>所以首先就是要记住创建验证人节点的时候提示的助记词。咱在之前那篇创建主网络和测试网络节点那篇文章里已经提醒过了的样子。</p><p>那么如果真的不幸的原有的节点丢失的时候呢？ 在创建密钥对那一步，可以加上 <code>--recover</code> 参数来从助记词计算私钥。</p><pre class="ql-syntax" spellcheck="false">docker-compose run --rm liked-command keys add <这里是密钥对的名称，一般会是 validator> --recover
</pre><p>然后按提示输入助记词和保护密钥环的密码。</p><p>不过如果汝当时没记下来助记词的话，也还是有办法导出私钥的。虽然咱好像没看到和其它钱包类似的重新显示助记词的方法来着。</p><p>这次要用到 <code>liked</code> 中的 <code>keys export</code> 命令：</p><pre class="ql-syntax" spellcheck="false">docker-compose run --rm liked-command keys export <这里是密钥对的名称，一般会是 validator>
</pre><p>然后按提示输入保护导出文件的密码和密钥环的密码，结果会输出在屏幕上，大概会像这个样子。</p><pre class="ql-syntax" spellcheck="false">-----BEGIN TENDERMINT PRIVATE KEY-----
kdf: bcrypt
salt: 1621DB2F53A59FDC2EDB9DD6D07FA8C0
type: secp256k1
​
L0PaGuvEsCPTLJ5FlQsoey98jQVLHp6fLFKS9ihXkkih1a+jpbYmRPVoq47kdjiF
jrNcV3DsLjUj6NiCiRyJ72zovqP7VlMTOQu4wUY=
=3K7B
-----END TENDERMINT PRIVATE KEY-----
</pre><p>把它的内容复制下来保存好，以及记住汝导出时使用的密码。</p><p>如果需要导入的时候，就在 likecoin-chain 的目录里建立一个文本文件，填上导出的内容。在下面的例子里就是 exported.asc 了。</p><p>然后用 <code>liked</code> 中的 <code>keys import</code> 命令导入：</p><pre class="ql-syntax" spellcheck="false">docker-compose run --rm liked-command keys export <这里是密钥对的名称，一般会是 validator> <这里是导出的私钥文件的路径>
</pre><p>但是这里的私钥文件的路径是对容器来说的路径，所以路径前面要加上在 docker-compose.yml 里设置好的映射到主机的路径，于是整个命令就会是这个样子：</p><pre class="ql-syntax" spellcheck="false">docker-compose run --rm liked-command keys export validator /host/exported.asc
</pre><p>然后按照提示输入导出时设置的密码和密钥环的密码。</p><blockquote>不过话说回来，要是汝有用过 openPGP 的话，这些操作应该不会陌生？</blockquote><p>以及重新同步状态也要花不少时间呢。所以如果硬盘空间充足的话，直接把整个 likecoin-chain 的目录复制一份出来也许更方便的样子，这个方法就当作后备了。</p><h2>那咱又是怎么做的呢……</h2><p>关于备份验证人节点的方法嘛，其实已经有验证人同仁们给出自己的解决方案了。例如 Nukken <a href="https://public.nnkken.dev/liked-data-archive/snapshot.sh" rel="noopener noreferrer" target="_blank">有一个脚本</a>每日生成验证人节点数据的快照。</p><p>咱的话，因为咱把仓库和验证人数据放在了一个 btrfs 子卷（btrfs 的子卷差不多是一种特殊的目录，可以作为挂载点独立挂载）里，所以很自然的就用 btrfs 的快照和发送/接收命令定期将子卷的数据发回到家里的 NAS 上。</p><blockquote>所以很自然的，咱的方法不一定对汝也合适，并不建议直接模仿。</blockquote><pre class="ql-syntax" spellcheck="false">sdc   8:32  0 200G 0 disk 
└─sdc1  8:33  0 200G 0 part /likecoin-chain
                /home/horo/likecoin-chain 
</pre><p>在咱这个例子里， /likecoin-chain 是整个 btrfs 卷，而 /home/horo/likecoin-chain 是其中一个子卷，所以 /likecoin-chain 目录大概像这个样子：</p><pre class="ql-syntax" spellcheck="false">horo@localhost ~ % ls /likecoin-chain
likecoin-chain likecoin-chain-20211128 likecoin-chain-20211129
...
</pre><p>出于不知道验证人节点运行的时候会更新什么文件，所以在备份之前需要先让节点停下来。</p><pre class="ql-syntax" spellcheck="false">docker-compose stop
</pre><p>然后创建快照：</p><blockquote># btrfs subvolume snapshot 原始子卷 快照子卷 加上 -r 参数的话，就会创建一个只读快照。 date 命令返回今天的日期和时间，也可以指定一个格式字符串来按某个特定的格式输出。 以 $ 包围的命令会以它的结果填充，例如 echo “root_$(date +”%Y%m%d”)” 的 结果是 root_20220213 （咱写完这篇文章的时间，汝自己运行的话结果肯定会和咱有变化）。</blockquote><pre class="ql-syntax" spellcheck="false"># btrfs subvolume snapshot -r likecoin-chain likecoin-chain-$(date +"%Y%m%d")
</pre><p>创建完快照以后就可以把节点重新开起来了，以及可以通过 <code>btrfs send</code> 和 <code>btrfs recieve</code> 在两个 btrfs 卷之间传送子卷（或子卷的快照），不过要是只读的才行：</p><pre class="ql-syntax" spellcheck="false"># btrfs send <path/to/your/subvolume> | btrfs recieve <path/to/your/save/place>
</pre><p>如果创建快照时忘记设置只读，可以通过 <code>btrfs property</code> 命令设置上（当然也可以取消只读）：</p><pre class="ql-syntax" spellcheck="false"># btrfs property set -ts <path/to/your/subvolume> ro [true|false]
</pre><p>汝也可以传递增量快照，就像这样：</p><pre class="ql-syntax" spellcheck="false"># btrfs send <path/to/your/subvolume> -p <path/to/your/parent_subvolume> | btrfs recieve <path/to/your/save/place>
</pre><p>不过汝要先把父快照传送到目标才行。 这个命令也能和 ssh 命令搭配使用，像这样：</p><pre class="ql-syntax" spellcheck="false"># btrfs send /likecoin-chain/likecoin-chain-20211128 | ssh root@somewhere "btrfs receive /data/backups/"
</pre><p>把上面的内容整理成一个 Shell 脚本，再搭配上 Crontab 或者 Systemd Timer，就可以定时备份了。要点就是 btrfs 的大部分命令需要以 root 用户运行，而定时运行的时候又不太方便输入 root 用户的密码（以及正经人不会允许 root 用密码登录 ssh 的），所以最好是设置一对密钥。</p><p>原文连结：<a href="https://blog.horo.moe/?p=34" rel="noopener noreferrer" target="_blank">备份 LikeCoin 验证人节点的二三事 - 约伊兹的萌狼乡手札</a></p>  
</div>
            