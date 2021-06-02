
---
title: 'OpenHarmony 2.0 Canary 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-ed922f61e32f960bdcdfdb074444732f277.png'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 07:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-ed922f61e32f960bdcdfdb074444732f277.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>6月1日，开放原子开源基金会（OpenAtom Foundation，以下简称“基金会”）正式发布 OpenAtom OpenHarmony（以下简称"OpenHarmony"） 2.0 Canary。</p> 
<p>全球开发者可通过 Gitee 下载完整代码：<a href="https://gitee.com/openharmony" target="_blank">https://gitee.com/openharmony</a></p> 
<p>OpenHarmony是由基金会孵化及运营的开源项目，由基金会的OpenHarmony项目群工作委员会负责运作，遵循Apache 2.0等开源协议，目标是面向全场景、全连接、全智能时代，基于开源的方式，搭建一个智能终端设备操作系统的框架和平台。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ed922f61e32f960bdcdfdb074444732f277.png" referrerpolicy="no-referrer"></p> 
<p>OpenHarmony 2.0 Canary 的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fg3q7IwTrM3Rm7y5-t-yxew" target="_blank">发布公告</a>写道：</p> 
<blockquote> 
 <p><strong>OpenHarmony 2.0 自主研发，不兼容安卓。</strong>OpenHarmony 用户应用程序是一种基于服务原子化概念定义的新型应用。与传统终端用户应用程序不同，OpenHarmony 用户应用程序支持在 OpenHarmony 设备间跨端迁移、多端协同，一次开发多端部署，实现可分可合可流转。</p> 
 <p>OpenHarmony 用户应用程序基于全新设计的 OpenHarmony API/SDK 开发，可以运行在基于全新 OpenHarmony 开源项目开发的系统上，并可以在多终端之间无缝流转。</p> 
 <p>OpenHarmony 程序框架仅支持全新的 OpenHarmony 用户应用程序运行，不支持基于安卓系统的 API/SDK 开发的用户应用程序运行。</p> 
</blockquote> 
<p>OpenHarmony 2.0 Canary 在 OpenHarmony 1.1.0 的基础上，增加标准系统版本，具备的主要功能如下：</p> 
<ul> 
 <li>新增22个子系统，支持全面的OS能力，支持内存大于128M的带屏设备开发等。</li> 
 <li>提供系统三大应用：桌面、设置和SystemUI。</li> 
 <li>提供全新的OpenHarmony应用框架能力、Ability Cross-platform Engine能力。</li> 
 <li>提供JS应用开发能力。</li> 
 <li>提供媒体框架，支持音视频功能开发。</li> 
 <li>提供图形框架能力，支持窗口管理和合成，支持GPU能力。</li> 
</ul> 
<h3>配套关系</h3> 
<p><strong>表 1</strong> 版本软件和工具配套关系</p> 
<table cellspacing="0"> 
 <thead> 
  <tr> 
   <th> <p>软件</p> </th> 
   <th> <p>版本</p> </th> 
   <th> <p>备注</p> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td> <p>OpenHarmony</p> </td> 
   <td> <p>2.0 Canary</p> </td> 
   <td> <p>NA</p> </td> 
  </tr> 
  <tr> 
   <td> <p>HUAWEI DevEco Studio（可选）</p> </td> 
   <td> <p>DevEco Studio 2.1 Release</p> </td> 
   <td> <p>OpenHarmony应用开发推荐使用。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>HUAWEI DevEco Device Tool（可选）</p> </td> 
   <td> <p>Deveco DeviceTool 2.2 Beta1</p> </td> 
   <td> <p>OpenHarmony智能设备集成开发环境推荐使用。</p> </td> 
  </tr> 
 </tbody> 
</table> 
<h3>更新说明</h3> 
<p>本版本完全继承了OpenHarmony 1.1.0的所有特性，并在OpenHarmony 1.1.0版本的基础上，新增标准系统版本形态，详情请参考下表 。</p> 
<p><strong>表 2</strong> 版本新增特性表</p> 
<table cellspacing="0"> 
 <thead> 
  <tr> 
   <th> <p>子系统名称</p> </th> 
   <th> <p>新增特性</p> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td> <p>内核</p> </td> 
   <td> <p>基于Linux Kernel LTS社区开源基线，回合CVE补丁，包含了OpenHarmony上层特性适配。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>分布式文件</p> </td> 
   <td> <p>提供本地同步文件 JS 接口，包括文件读写、目录访问以及文件Stat。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>图形图像</p> </td> 
   <td> 
    <ul> 
     <li>新增窗口管理功能，包括创建、销毁和窗口栈管理等。</li> 
     <li>新增合成器功能，包括CPU、GPU和TDE合成。</li> 
     <li>新增bufferqueue功能，支持进程间传递。</li> 
     <li>新增vsync管理功能。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>驱动</p> </td> 
   <td> <p>新增用户态驱动框架。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>电源管理服务</p> </td> 
   <td> <p>新增电源管理能力，包括关机服务、亮灭屏管理、亮度调节、电池状态查询、系统电源管理、休眠锁管理等功能。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>多模输入子系统</p> </td> 
   <td> <p>新增支持单指触屏输入能力。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>启动恢复子系统</p> </td> 
   <td> <p>系统属性管理新增JS API。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>升级服务</p> </td> 
   <td> 
    <ul> 
     <li>新增recovery系统升级服务能力。</li> 
     <li>新增差分包升级能力。</li> 
     <li>新增系统属性管理JS API。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>帐号</p> </td> 
   <td> <p>提供分布式云帐号登录状态管理功能。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>编译构建</p> </td> 
   <td> 
    <ul> 
     <li>支持按照部件名或模块名编译指定目标。</li> 
     <li>支持不同芯片平台接入，配置产品部件列表。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>测试</p> </td> 
   <td> <p>新增开发者自测试能力，支持C++ API单元测试，API性能测试等。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>数据管理</p> </td> 
   <td> <p>提供轻量级Key-Value操作，支持本地应用存储少量数据，数据存储在本地文件中，同时也加载在内存中的，所以访问速度更快，效率更高。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>语言编译运行时</p> </td> 
   <td> <p>提供了JS、C/C++语言程序的编译、执行环境，提供支撑运行时的基础库，以及关联的API接口、编译器和配套工具。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>分布式任务调度</p> </td> 
   <td> <p>提供系统服务的启动、注册、查询及管理能力。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>JS UI框架</p> </td> 
   <td> 
    <ul> 
     <li>提供40+UI基础组件和容器组件。</li> 
     <li>提供标准CSS动画。</li> 
     <li>支持原子化布局、栅格布局。</li> 
     <li>提供类Web开发范式的UI编程框架。</li> 
     <li>JS API扩展机制。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>媒体</p> </td> 
   <td> 
    <ul> 
     <li>新增媒体播放和录制基本功能。</li> 
     <li>新增相机管理和相机采集基本功能。</li> 
     <li>新增音频音量和设备管理基本功能。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>事件通知</p> </td> 
   <td> <p>新增发布、订阅、接收公共事件的基本功能。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>杂散软件服务</p> </td> 
   <td> <p>新增设置时间的能力。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>用户程序框架</p> </td> 
   <td> <p>新增包安装、卸载、运行及管理能力。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>电话服务</p> </td> 
   <td> 
    <ul> 
     <li>新增获得信号强度、获得驻网状态能力。</li> 
     <li>新增获得SIM卡状态能力。</li> 
     <li>新增拨打电话、拒接电话、挂断电话能力。</li> 
     <li>新增发送短信、接收短信能力。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>公共基础类库</p> </td> 
   <td> <p>提供了一些常用的C、C++开发增强API。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>研发工具链</p> </td> 
   <td> 
    <ul> 
     <li>新增设备连接调试器。</li> 
     <li>新增性能跟踪能力。</li> 
     <li>新增实时内存和trace调优工具，和端侧插件能力。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>分布式软总线</p> </td> 
   <td> 
    <ul> 
     <li>新增跨进程通信(IPC)和跨设备的远程过程调用(RPC)能力。</li> 
     <li>新增支持设备发现、组网、传输能力的软总线服务。</li> 
     <li>新增WiFi服务，可提供STA开关、扫描、连接等基本能力。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>XTS</p> </td> 
   <td> <p>新增各业务特性公共API兼容性看护用例套件。</p> </td> 
  </tr> 
  <tr> 
   <td> <p>系统应用</p> </td> 
   <td> <p>桌面:</p> 
    <ul> 
     <li>新增全量应用图标展示、启动和卸载应用能力。</li> 
     <li>新增桌面管理界面，可切换网格布局与列表布局。</li> 
     <li>新增最近任务管理能力，可热启动和清理任务。</li> 
    </ul> <p>设置：</p> 
    <ul> 
     <li>新增设置应用，包括亮度设置，应用信息，时间设置和关于设备。</li> 
    </ul> <p>SystemUI：</p> 
    <ul> 
     <li>新增系统栏展示，包括时间、电量信息。</li> 
     <li>新增系统导航展示。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>DFX</p> </td> 
   <td> 
    <ul> 
     <li>新增流水日志。</li> 
     <li>新增应用故障收集和订阅。</li> 
     <li>新增系统事件记录接口。</li> 
     <li>新增应用事件记录接口及框架。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>全球化子系统</p> </td> 
   <td> 
    <ul> 
     <li>新增支持资源解析读取能力。</li> 
     <li>新增支持时间日期格式化能力。</li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td> <p>安全</p> </td> 
   <td> 
    <ul> 
     <li>新增系统权限管理，包括系统权限声明，应用安装时申请或申明的权限解析，权限查询，权限授予。</li> 
     <li>新增应用签名和验签能力。</li> 
     <li>新增点对点设备连接时的互信认证能力和设备群组管理能力。</li> 
    </ul> </td> 
  </tr> 
 </tbody> 
</table> 
<p><a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/release-notes/OpenHarmony-2-0-Canary.md" target="_blank">详情点此查看</a>。</p> 
<hr> 
<h1>OpenHarmony 大事记</h1> 
<h2><strong>2020年9月</strong></h2> 
<p>2020年9月开放原子开源基金会（OpenAtom Foundation，以下简称“基金会”）获捐OpenHarmony开源项目后宣布开源，随后组织各方力量对项目开展共建，于2020年12月联合七家志愿共建单位成立了OpenHarmony项目群工作委员会，七家单位分别是（排名按单位简称首字母排序）：博泰、华为、京东、润和、亿咖通、中科院软件所、中软国际。</p> 
<p>OpenHarmony开源项目重大事项由工作委员会各成员单位代表用投票方式共同决定，投票权利均等，一家单位一票，遵循公开明确的OpenHarmony项目群管理制度规则。按照约定的规则与流程，贡献者随时可以在OpenHarmony开源项目gitee社区贡献代码，开放原子开源基金定期组织版本发布。</p> 
<h2><strong>2020年9月10日</strong></h2> 
<p>2020年9月10日，OpenHarmony 1.0 版本正式上线，支持内存为128K到128M的终端设备。</p> 
<h2><strong>截至2021年5月</strong></h2> 
<p>截至2021年5月，信通院泰尔实验室、好叭科技、华秋电子、软通动力、思必拓科技等单位陆续协商加入项目群，正在完成协议签署和捐款流程。</p> 
<h2><strong>2021年6月1日</strong></h2> 
<p>2021年6月1日，OpenHarmony 2.0 Canary版本宣布上线，支持内存128M以上的各种智能终端设备。</p> 
<p>OpenHarmony 2.0 自主研发，不兼容安卓。众多开发合作伙伴将以开源社区为中心，分阶段快速迭代，不断完善系统能力，逐步构建起面向万物互联时代的OpenHarmony生态。在全球范围内有兴趣、有需要的组织和个人都可以基于开源项目的章程参与OpenHarmony开源项目，实现共商、共建、共享、共赢。截至2021年5月31日，已有240多个共建企业、共建机构与个人贡献者参与项目。</p> 
<p>OpenHarmony在开放原子开源基金会的组织下、在OpenHarmony项目群工作委员会的治理下，以工作组、特别兴趣小组、子项目形式等方式组织（特别兴趣小组简称SIG，英文全称Special Interest Group，具体运作及参与共建方式见：<a href="https://gitee.com/openharmony/community/tree/master/sig" target="_blank">https://gitee.com/openharmony/community/tree/master/sig</a>）。</p> 
<p>【开放原子开源基金会】开放原子开源基金会是致力于推动全球开源产业发展的非营利机构，于2020年6月正式获得民政部批准在北京成立，由阿里巴巴、百度、华为、浪潮、360、腾讯、招商银行等十家龙头科技企业联合发起，由工信部作为业务指导单位。开放原子开源基金会拟通过共建、共治、共享的方式，系统性打造信息产业和工业开源开放框架，搭建国际开源社区，提升行业协作效率，赋能千行百业。目前开放原子开源基金会业务范围主要包括为各类开源软件、开源硬件、开源芯片、开源内容提供中立的知识产权托管、战略咨询、法务咨询、项目运营、品牌营销和教育培训等服务。</p>
                                        </div>
                                      
</div>
            