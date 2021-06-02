
---
title: 'OpenHarmony 2.0 Canary 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2367'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2367'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenHarmony 2.0 Canary 现已发布，当前版本在 OpenHarmony 1.1.0 的基础上，增加标准系统版本，具备的主要功能如下：</p> 
<ul> 
 <li>新增22个子系统，支持全面的OS能力，支持内存大于128M的带屏设备开发等。</li> 
 <li>提供系统三大应用：桌面、设置和SystemUI。</li> 
 <li>提供全新的OpenHarmony应用框架能力、Ability Cross-platform Engine能力。</li> 
 <li>提供JS应用开发能力。</li> 
 <li>提供媒体框架，支持音视频功能开发。</li> 
 <li>提供图形框架能力，支持窗口管理和合成，支持GPU能力。</li> 
</ul> 
<h4>配套关系</h4> 
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
<h4>更新说明</h4> 
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
<p>详情可见：<a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/release-notes/OpenHarmony-2-0-Canary.md">https://gitee.com/openharmony/docs/blob/master/zh-cn/release-notes/OpenHarmony-2-0-Canary.md</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            