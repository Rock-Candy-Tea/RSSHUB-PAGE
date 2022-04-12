
---
title: 'openEuler 22.03 内置 openGauss，一键安装提高用户易用性！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5a457a012723d11c7135d24290c014c321a.png'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 01:44:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5a457a012723d11c7135d24290c014c321a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0; margin-right:0"><strong>2022年3月，openEuler 22.03 LTS版本ISO安装包仓库及LTS官方软件仓库均上线openGauss2.1.0版本安装包，提供RPM一键安装openGauss的能力，提高用户易用性。</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>openGauss软件包使用，提供用户易用性</strong></p> 
<p style="margin-left:0; margin-right:0">openEuler 22.03 LTS版本中涉及的openGauss安装包及其依赖仓库如下：</p> 
<p style="margin-left:0; margin-right:0">https://gitee.com/src-openeuler/opengauss-server</p> 
<p style="margin-left:0; margin-right:0">https://gitee.com/src-openeuler/opengauss-dcf</p> 
<p style="margin-left:0; margin-right:0"><strong>openGauss ISO软件包使用概述</strong></p> 
<p style="margin-left:0; margin-right:0"><strong>方式一：安装操作系统时勾选数据库</strong></p> 
<p style="margin-left:0; margin-right:0">在使用openEuler 22.03 LTS ISO镜像安装操作系统时候，安装引导界面的选择软件包里面勾选上openGauss Server，在安装完成操作系统后，便会默认安装上openGauss数据库并启动单机数据库进程。</p> 
<p><img alt height="405" src="https://oscimg.oschina.net/oscnet/up-5a457a012723d11c7135d24290c014c321a.png" width="1001" referrerpolicy="no-referrer"></p> 
<p><img alt height="485" src="https://oscimg.oschina.net/oscnet/up-8dcd6a13d3d31d5ffb25ecbefa71f84e23d.png" width="1009" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0; margin-right:0"><strong>方式二：安装完操作系统后使用yum一键安装</strong></p> 
<p style="margin-left:0; margin-right:0">如果在安装操作系统时候没有选择openGauss软件包，还可以在安装完系统后，通过命令一键安装上openGauss的单机数据库实例：</p> 
<pre><code>
yum install opengauss -y</code></pre> 
<p style="margin-left:0; margin-right:0">使用说明：</p> 
<p style="margin-left:0; margin-right:0">openGauss数据库进程的管理用户为opengauss，切换到该用户下可以进行数据库的常用操作。</p> 
<pre><code>
su - opengauss</code></pre> 
<p><span style="background-color:#ffffff; color:#222222">登录数据库中执行sql语句：</span></p> 
<pre><code>
gsql -d postgres -r</code></pre> 
<p><span style="background-color:#ffffff; color:#222222">查询数据库实例状态：</span></p> 
<pre><code>
gs_ctl query</code></pre> 
<p><span style="background-color:#ffffff; color:#222222">停止数据库实例进程：</span></p> 
<pre><code>
gs_ctl stop</code></pre> 
<p><span style="background-color:#ffffff; color:#222222">启动数据库实例进程：</span></p> 
<pre><code>
gs_ctl start</code></pre> 
<p style="margin-left:0; margin-right:0"><strong>openGauss RPM软件包使用概述</strong></p> 
<p style="margin-left:0; margin-right:0">概述为使用非openEuler 22.03 LTS ISO软件包的用户，需要配置openEuler 22.03 LTS官方源。</p> 
<p style="margin-left:0; margin-right:0"><span><strong>Step.1</strong></span></p> 
<p style="margin-left:0; margin-right:0">针对不同硬件平台(aarch64/x86_64)在本地添加openEuler 22.03 LTS everything 软件仓库，openGauss软件包所处位置为：</p> 
<p style="margin-left:0; margin-right:0">https://repo.openeuler.org/openEuler-22.03-LTS/everything/</p> 
<p style="margin-left:0; margin-right:0">配置完成后，执行</p> 
<pre><code>
dnf update</code></pre> 
<p style="margin-left:0; margin-right:0">在本地更新远端仓库。</p> 
<p style="margin-left:0; margin-right:0"><span><strong>Step.2</strong></span></p> 
<p style="margin-left:0; margin-right:0">安装openGauss软件包及其对应依赖包。</p> 
<pre><code>
dnf install opengauss -y</code></pre> 
<p style="margin-left:0; margin-right:0">安装完成后：</p> 
<p style="margin-left:0; margin-right:0">openGauss的安装路径在 /usr/local/opengauss</p> 
<p style="margin-left:0; margin-right:0">首先来看openGauss环境变量，启动openGauss和连入服务需要的环境变量被放置在 /var/lib/opengauss/.bash_profile</p> 
<pre><code>
export GAUSSHOME=/usr/local/opengauss/
export LD_LIBRARY_PATH=/usr/local/opengauss/lib:$LD_LIBRARY_PATH
export PATH=/usr/local/opengauss/bin:$PATH
export PGDATA=/var/lib/opengauss/data
export PORT=7654</code></pre> 
<p style="margin-left:0; margin-right:0">从这些环境变量，可以直观地看到openGauss的安装路径，DATA PATH，依赖库路径等等。</p> 
<p style="margin-left:0; margin-right:0">另外，openGauss轻量化构建选项opengauss_config_file_mini，被放在/usr/local/opengauss/share/postgresql/</p> 
<p style="margin-left:0; margin-right:0">默认启动的配置文件在 /usr/local/opengauss/share/postgresql/postgresql.conf.sample，可以按需修改或重新指定。</p> 
<p style="margin-left:0; margin-right:0">Systemd相关文件存放在 /usr/local/opengauss/script/</p> 
<p style="margin-left:0; margin-right:0"><span><strong>Step.3</strong></span></p> 
<p style="margin-left:0; margin-right:0">在openGauss软件包安装成功后，会为其创建opengauss用户用来运行openGauss服务。接下来就可以使用：</p> 
<pre><code>
systemctl start opengauss</code></pre> 
<p style="margin-left:0; margin-right:0">启动openGauss单节点环境。</p> 
<p style="margin-left:0; margin-right:0"><strong>   Notes:</strong></p> 
<p style="margin-left:0; margin-right:0">1. 安装前需要确定系统中没有opengauss同名用户存在，以免产生安装冲突；</p> 
<p style="margin-left:0; margin-right:0">2. 当前只支持openGauss单节点环境安装，更多配置参考openGauss社区官方文档；</p> 
<p style="margin-left:0; margin-right:0">3. 如需修改openGauss配置文件或systemd启动脚本，参考</p> 
<pre><code>
/usr/local/opengauss/script/opengauss.service
/usr/local/opengauss/script/autostart.sh</code></pre> 
<p style="margin-left:0; margin-right:0">进行添加适配；</p> 
<p style="margin-left:0; margin-right:0">4. 新添配置或目录需要给予opengauss用户相应权限。</p> 
<p style="margin-left:0; margin-right:0"><strong>双方社区成员通力合作，为社区间合作提供范例</strong></p> 
<p style="margin-left:0; margin-right:0">此次两大社区能够顺畅地完成目标，得益于双方社区成员的通力合作。来自openGauss社区的committer-<span style="color:#7a1ae1">张旭博</span><span>(https://gitee.com/zhang_xubo)</span><span> </span>与openEuler DB SIG maintainer- <span style="color:#7a1ae1">赵波</span><span>(https://gitee.com/bzhaoop)</span><span> </span>以公开透明的形式将本次合作落实在开源社区中，所完成的任务和讨论均符合开源社区贡献流程，包括TC例会讨论，Issue及PR提交等。下面是对本次工作内容的简要介绍，希望可以为未来相关社区间的合作提供参考。</p> 
<p style="margin-left:0; margin-right:0"><strong>1.openGauss社区2.1.0发布包引入openEuler 22.03 LTS</strong></p> 
<p style="margin-left:0; margin-right:0">此次进入openEuler构建和发布的软件包均来自openGauss社区及相应依赖软件包的上游社区，涉及openGauss 2.1.0版本，链接如下：</p> 
<p style="margin-left:0; margin-right:0">https://gitee.com/opengauss/openGauss-server</p> 
<p style="margin-left:0; margin-right:0">https://gitee.com/opengauss/DCF</p> 
<p style="margin-left:0; margin-right:0">此次参与openEuler构建和发布的包来自openGauss社区发布包(openGauss-server-2.1.0.tar.gz)，链接如下：</p> 
<p style="margin-left:0; margin-right:0">https://gitee.com/opengauss/openGauss-server/tree/2.1.0/</p> 
<p style="margin-left:0; margin-right:0">https://gitee.com/opengauss/openGauss-server/releases/v2.1.0</p> 
<p style="margin-left:0; margin-right:0">软件包的引入和提交到openEuler社区的PR均由openGauss社区和openEuler DB SIG协作完成，相关的软件包质量和维护由openGauss社区和openEuler DB SIG共同保障。</p> 
<p style="margin-left:0; margin-right:0"><strong>2.工作重点</strong></p> 
<p style="margin-left:0; margin-right:0">本次工作重点主要为几个方面：</p> 
<p style="margin-left:0; margin-right:0"><strong>1）openGauss依赖分析及梳理</strong></p> 
<p style="margin-left:0; margin-right:0">由于openGauss社区本身体系较为庞大，对于通用型数据库来说，所发布自身软件时依赖的其他软件均来自上游社区，并且对部分功能进行一定程度的功能性增强，故部分依赖库与openEuler软件仓库已有的上游社区发布版本冲突，这一部分已经由openGauss社区单独在其社区内部及openEuler软件仓库中单独进行维护。此次合作中，已将全部依赖库引入openEuler软件仓库，完全融入openEuler软件生态当中。</p> 
<p style="margin-left:0; margin-right:0"><strong>2）openGauss易用性脚本引入</strong></p> 
<p style="margin-left:0; margin-right:0">本次的openGauss RPM包引入，为了保留用户使用习惯，延用systemd服务，对openGauss服务进行了全面适配，包括服务启动控制脚本，另外，还提供了openGauss冷升级脚本等，并在openGauss RPM软件包安装过程中进行了与openGauss社区文档所述相同的配置，例如运行用户及相应的配置等，极大方便用户在openEuler上使用openGauss的安装成本，达成一键安装功能。</p> 
<p style="margin-left:0; margin-right:0"><strong>3. 后续工作</strong></p> 
<p style="margin-left:0; margin-right:0">1)为了能够更加深入两方社区合作，从提高用户的易用性出发，计划在openEuler及openGauss两个社区增加RPM方式安装openGauss软件的文档，为用户提供多种安装方式；</p> 
<p style="margin-left:0; margin-right:0">2)随着上游openGauss社区发布版本的持续迭代，需要持续在openEuler软件仓库中更替最新版openGauss软件，并计划在最新版openEuler发布版中发布，例如最新版openGauss版本将计划在同样为最新版的openEuler发布版中进行发布，供用户提前体验，如openGauss 3.0.0(已于今年4月发布)计划将在今年openEuler 22.09创新版中发布，同时保留在openEuler LTS（22.03 LTS）版本中的openGauss（2.1.0）版本；</p> 
<p style="margin-left:0; margin-right:0">3)如果你对后续计划感兴趣，欢迎到社区官网签署CLA，参与贡献。</p> 
<p style="margin-left:0; margin-right:0"><strong>两大社区相互赋能，共同铸就丰富多样的软件生态</strong></p> 
<p style="margin-left:0; margin-right:0; text-align:justify">openGauss社区与openEuler社区作为两个开源开放的社区，通过相互协作和融合，使得openGauss进入openEuler 22.03 LTS ISO镜像，同时为openEuler 22.03 LTS官方仓库提供openGauss软件包，极大地提高了openGauss用户易用性；同时，也为使用openEuler 22.03 LTS ISO及其他镜像源的用户带来了便利。</p> 
<p style="margin-left:0; margin-right:0">未来，openGauss和openEuler社区将继续加深合作，持续在openEuler软件仓库中维护openGauss的迭代版本，为openGauss软件的质量提供保障。随着openGauss功能、性能的持续迭代，openGauss日益成熟，秉承共建、共享、共治的理念，被越来越多的用户认可。此次通过与openEuler开源社区的相互合作，提高openGauss的易用性，相信openGauss会成为更多用户的选择，也欢迎更多的人加入openGauss和openEuler社区，共同铸就丰富多样的基础软件生态。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>openGauss：</strong>openGauss是一款开源关系型数据库管理系统，采用木兰宽松许可证v2发行。openGauss内核深度融合华为在数据库领域多年的经验，结合企业级场景需求，持续构建竞争力特性。同时openGauss也是一个开源的数据库平台，鼓励社区贡献、合作。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>openEuler：</strong>openEuler是一款开源操作系统。当前openEuler内核源于Linux，支持鲲鹏及其它多种处理器，能够充分释放计算芯片的潜能，是由全球开源贡献者构建的高效、稳定、安全的开源操作系统，适用于数据库、大数据、云计算、人工智能等应用场景。同时，openEuler是一个面向全球的操作系统开源社区，通过社区合作，打造创新平台，构建支持多处理器架构、统一和开放的操作系统，推动软硬件应用生态繁荣发展。</p>
                                        </div>
                                      
</div>
            