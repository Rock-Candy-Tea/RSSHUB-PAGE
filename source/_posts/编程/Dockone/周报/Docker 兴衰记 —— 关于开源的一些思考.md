
---
title: 'Docker 兴衰记 —— 关于开源的一些思考'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9470'
author: Dockone
comments: false
date: 2021-05-10 04:06:38
thumbnail: 'https://picsum.photos/400/300?random=9470'
---

<div>   
<br><blockquote><br>Docker support in the kubelet is now deprecated and will be removed in a future release. The kubelet uses a module called “dockershim” which implements CRI support for Docker and it has seen maintenance issues in the Kubernetes community. We encourage you to evaluate moving to a container runtime that is a full-fledged implementation of CRI (v1alpha1 or v1 compliant) as they become available. (#94624, @dims) [SIG Node]</blockquote>上述引言来自 Kubernetes 1.120 的 Release Note，标志着 Docker 的丧钟进入尾声。事实上，当 2018 年 Docker 创始人 CTO Solomon Hykes 宣布离职时，Docker 和公司的命运已是江河日下。在复杂商业利益的驱使和一意孤行的错误决策下，从 2016 年至今诞生了 CRI、OCI 等标准和 Containerd、Runc、Docker-shim、CRI-O 等眼花缭乱却、功能盘龙交错重叠的项目，Kubelet 和容器运行时的调用链路复杂冗长且多次变化，整个生态为此苦不堪言。<br>
<br>回想 1981 年 IBM 推出 PC 时，采用了非常开放的标准，凝聚了硬件和软件的生态，迅速占据市场第一把交椅。开放也导致了广大廉价而有竞争力的兼容机出现，渐渐蚕食 IBM 的市场份额。于是 1987 年 IBM 从开放走向封闭，推出一款不再兼容外部硬件的机器 IBM PS/2，彻底走上了一条不归路，失去市场的同时失去了 PC 产业话语权。让我们再次回顾 Docker 从一鸣惊人再到由盛而衰的历史，并思考开源商业、技术和文化和内在逻辑和一些教训。<br>
<h3>小船出海</h3>PaaS 历来是兵家必争之地，通过类似 Container 技术将应用封装并交由编排系统管理，将给 DevOps 带来巨大的效率和成本优化。2002 年诞生的 linux namespace 和 2006 年诞生的 cgroup 为此奠定基本技术基础，此后 Google 和百度依次建设了 Borg 和 Matrix 平台，并取得巨大的成功；与此同时开源界也诞生了 Cloud Foundry 等项目。但在外人看来，Borg 和 Matrix 只闻其名，未见其实；而 Cloud Foundry 一直不愠不火，未得到广泛的普及。<br>
<br>究其根本原因乃是对应用(交付)的标准抽象的不过友好。以 Cloud Foundry 为例，它针对每种语言指定了一系列的标准，比如目录、可执行文件、二进制等等。这用在内部场景用无可厚非，绝大部分上规模的公司都会为应用设定一系列的规则，比如编码、配置、打包、运行环境和依赖，并形成各自的特色的标准；但是放眼整个生态，这种要求过于苛刻而缺乏普及性。Docker 真正革命之处在于开创了基于镜像交付应用的先河，它把应用的代码、配置和所有用户态层次依赖的整合成一个镜像，保证了运行环境的高度闭环和统一，对宿主机的依赖仅限于内核，而内核的 posix 接口非常稳定和兼容，所以保证了 Docker 镜像具有一次制作，四处运行的强大兼容强大威力。<br>
<br>2013 年，成立三年的 dotCloud（Docker 公司前身）在 PaaS 平台产品商业化走到穷途末路时选择了开源核心引擎 Docker，换来的是柳暗花明又一村。这种轻量级虚拟化、语音无关、可移植性强的技术给出完美的应用交付标准，直击用户痛点，立马一石激起千层浪。这一年，Docker 迅速成长为云计算领域最受欢迎的项目，诸多巨头逐步增加了对 docker 的支持，很多应用软件的交付也提供了 docker 镜像；这一年，dotCloud 更名为 Docker，注册了 Docker 商标，出售了 PaaS 平台产品，全力转向 Docker 技术研发和生态建设。<br>
<br>此后的两年里，Docker 的发展可谓顺风顺水，生态版图持续扩大，从 Linux 到 Windows，从云计算到广义的应用市场，已俨然成为容器的标准。即使 Google 和 CoreOS 强势推出竞品 lmctfy 和 rkt，面对已成气候的 Docker 毫无招架之力。伴随生态的成功，Docker 前后拿下 4000 万刀和 9500 万刀的两轮重要融资补充粮草。当 2016 年夏天 DockerCon 举办时，Docker Hub 镜像总下载数量高达 40 多亿次，甚至一度传出微软欲以 40 亿美金收购这家只有数百人的公司！<br>
<h3>群雄逐鹿</h3>技术的持续发展离不开商业化的支持，Docker 作为一家创业公司从出身就背负着商业化的根本任务。尽管取得生态和技术上的巨大成功，带来了普世的巨大价值，却面临着商业化的巨大挑战。和其它通用而基础的开源技术一样，比如操作系统 Linux、编译工具 gcc、虚拟化技术 qemu-kvm，开源决定了 Liscense 之路不通，而单一的技术无法带来服务的溢价。打造 PaaS 平台层次的产品便成最具备可行性之路，和 2013 年卖掉 PaaS 平台相反，2014 年 Docker 收购 Fig 项目，以此推出编排产品 Docker Swarm，拉开了编排领域群雄逐鹿的帷幕。<br>
<br>开源的长河充满了合作和竞争，推动着生态不断发展和演进。这一年，Mesos 背后的公司 Mesospheres 推出 Marathon 项目；Google 基于 Borg 推出开源版本的编排项目 Kubernetes。和 Google、Redhat 等深谙道理的老玩家相比，年少气盛的 Docker 公司显得不易相处，2014 年 Docker 项目最早积极贡献者 CoreOS 不久后分道扬镳，和 Google、Redhat 创建了 OCI 规范，定义了容器运行时标准，妥协之下 Docker 公司从 libcontainer 捐献出 RunC 项目作为符合 OCI 标准的容器运行时。2015 年 Google、Redhat 等共同发起了 CNFC 基金会，并迅速增加了 Prometheus、etcd、Helm、CNI 等众多知名项目，生态发展的风向标逐步由 Docker 转向 Kubernetes，开始建造了坚固的护城河。<br>
<br>当时间来到 2016 年时，一切尘埃落定，远去了鼓角争鸣，Kubernetes 已成了容器编排领域的绝对标准。和暴发户 Docker 如日中天变得专横独断相比，Kubernetes 民主化的风格和 Plugin 的架构迅速的吸引了周边的生态伙伴；其次 Kubernetes 源自于 Google 基础设施领域多年的宝贵实践和升华，其设计的理念和抽象形态更贴近本质的需求。<br>
<br>即使 Kubernetes 赢得编排的标准，由于 Docker 已成容器的标准，所以早期的 Kubelet 内嵌 Docker 客户端，默认其为容器的运行时，因而从 Kubelet 到容器运行时的代码整体比较路径简短优雅 —— 容器的归容器、编排的归编排。但之后 Docker 公司祭出以自杀八百、损敌一千的姿态做出损人不利己的骚招。在面对 Swarm 的失败后，由于 Docker 名声和美誉广为人知，于是公司将 PaaS 平台的能力沉淀到名为 Docker 产品（甚至集成了 Kubernetes），并将 Docker 项目改名为 Moby，压上名气这张最后的筹码孤注一掷。<br>
<br>群雄逐鹿过程中，Docker 和 Kubernetes 之间的纠葛埋下广大同行深受其苦的坑，从 Kubelet 到运行时主要经历了如下调用链路的变更，诞生了一堆临时和更多凑热闹的项目，给广大的开发者带来沉重的心智负担，留下一地鸡毛。<br>
<pre class="prettyprint">+-----------------------+    +---------+    +-----------+<br>
| Kubelet(Dockerclient) | -> | Dockerd | -> | Container |<br>
+-----------------------+    +---------+    +-----------+<br>
<br>
+--------------+    +-------------+    +---------+    +------------+    +------+    +------------+<br>
| Kubelet(CRI) | -> | Docker-shim | -> | Dockerd | -> | Containerd | -> | Runc | -> | Containers |<br>
+--------------+    +-------------+    +---------+.   +------------+    +------+    +------------+<br>
<br>
+--------------+    +----------------+    +------------+    +------+    +-----------+<br>
| Kubelet(CRI) | -> | CRI-Containerd | -> | Containerd | -> | RunC | -> | Container | <br>
+--------------+    +----------------+    +------------+    +------+    +-----------+<br>
<br>
+--------------+    +------------+    +------+    +-----------+<br>
| Kubelet(CRI) | -> | Containerd | -> | RunC | -> | Container | <br>
+--------------+    +------------+    +------+    +-----------+<br>
</pre><br>
<h3>最佳选择</h3>有些历史被成为绝唱，那是因为没如果和重来。但是似曾相识的故事总是在不断的轮回，上世纪八十年代，蓝色巨人坐拥拥无人可撼动的市场霸主地位，当它试图以一己之力关闭兼容机的大门时，换来了作茧自缚。巅峰时期的 Docker 在生态上虽然取得了巨大的成功，但它的地位和当年的 IBM 丝毫不能相提并论，当然，这也是马后炮式的分析。<br>
<br>让我们站在 Docker 的曾经的巅峰上，俯瞰整个应用的交付标准唯我独尊，Docker hub 囊括了海量应用镜像，和下一个“VMware”相比，微软抛出区区 40 亿美金收购的橄榄枝又是多么的微不足道，我想换成任何人都愿意跃跃欲试，放手一搏向 PaaS 平台进军。当错失闪烁瞬间的机会后，便是土崩瓦解般的故事，2018 年创始人兼 CTO 离职，2019 年裁员，2020 年 Docker Hub 离奇的推出限速下载。<br>
<br>从商业的视角来看，基础而通用的开源技术项目本身价值和需求重大，但是成功的商业故事却寥寥无几。开源注定卖 License 之路不通，单一的基础技术很难带来服务的溢价，技术培训、二次开发的收益则是杯水车薪，而捐助等对于一家数百人的公司更天方夜谭，所以特别对于基础通用的技术来说，开源几乎不可能成为商业模式。但是从另外一个角度来说，开源更是一种市场策略，它可以快速试错，推广产品和思路，获得用户粘性，构建生态的护城河。如果顺着这个思路，从短期盈利的价值来看，Docker 公司卖给微软和 AWS 是中策，背靠着金主爸爸和强大的云计算服务；从长远的生态和普世价值角度来看，我认为 RedHat 收购 Docker 应该是最佳的选择，以 RedHat 的智慧，或将带来全方位的共赢和持久的繁荣。可以说，对于绝大部分做基础通用的开源技术产品的创业公司来说，被巨头收购已是最好的结局。<br>
<br>正如《大教堂和集市》所言：“开放式的文化会最终胜利，这或许不是因为”开放”在道德上正确，或者”封闭”在道德上错误，而只是因为开放式合作可以在一个问题上投入多几个数量级的技术工时，封闭的世界无法赢得这样的竞争。”当 Docker 开源时，它以新颖的理念解决应用交付的巨大痛点，描绘了 PaaS 的新蓝图，吸引了广泛的合作者。但是 Docker 的管理者既没有充分的识别和吸收他人优秀的想法，更没有良好的人际关系、交流技能和人格魅力。先后和 CoreOS、Redhat、Google 等开源巨头分道扬镳，最后又为一己之利和生态背离。开源生态的发展如一股大洪流滚滚向前，只能顺势和引领，不可阻挡，妄图借垄断之势损坏普遍大众的利益的行为只会被这股洪流冲垮和抛弃。<br>
<br>回首这八年，Docker 已到棺盖定论之时，它掀起了一场轰轰烈烈的 PaaS 革命，给 DevOps、云原生等带来了巨大的理念突破和奠定技术基础；而管理者的战略和战术的种种失误措施良机，接连败北，丢失了商业市场，失去了生态和名声，拉下一地鸡毛。数年以后，容器一词依旧盛行，而 Docker 或将无人提及，唯有一声叹息。<br>
<br>原文链接：<a href="http://wsfdl.com/" rel="nofollow" target="_blank">http://wsfdl.com/</a>编程随想/2021/03/09/docker_story.html，作者：koala bear
                                
                                                              
</div>
            