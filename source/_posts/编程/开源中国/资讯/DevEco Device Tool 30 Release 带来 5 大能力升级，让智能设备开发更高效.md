
---
title: 'DevEco Device Tool 3.0 Release 带来 5 大能力升级，让智能设备开发更高效'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c64ca8ced19ba2f588e16c38c738a1deb36.gif'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 09:10:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c64ca8ced19ba2f588e16c38c738a1deb36.gif'
---

<div>   
<div class="content">
                                                                                            <p><span>DevEco Device Tool是面向智能设备开发者提供的一站式集成开发环境，支持OpenHarmony/HarmonyOS Connect的组件按需定制，支持代码编辑、编译、烧录和调试、性能监测等功能，支持C/C++语言，以插件的形式部署在Visual Studio Code（简称VSCode）上，支持Windows10 64位或Ubuntu18.04-21.10版本。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>本次为大家带来的是DevEco Device Tool 3.0 Release版本新增及增强的五项功能，欢迎大家升级体验！</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>升级方式</span></strong></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#7f7f7f"><strong><span style="color:#7f7f7f">建议您从官网下载安装包进行全量升级：</span></strong></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f">https://device.harmonyos.com/cn/develop/ide#download_beta</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>一、支持产品化配置自动创建</span></span></strong></p> 
<p><span style="color:#333333">在进行设备开发时，开发者如果想要基于某一款开发板进行产品化开发，往往需要在已下载的源码基础上手动删除多余的文件、手动修改目录名称和config.json来进行产品工程初始化，导致开发效率不高。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>为了解决上述问题，新版本DevEco Device Tool<strong>支持根据输入继承的开发板名称和产品名称自动创建产品化开发所需要的最小文件集合和目录结构</strong>，无多余文件，无需手动删除，可直接进行产品化开发。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>具体使用方法：</span></strong></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:center"><img alt src="https://oscimg.oschina.net/oscnet/up-c64ca8ced19ba2f588e16c38c738a1deb36.gif" referrerpolicy="no-referrer"><img alt src="https://oscimg.oschina.net/oscnet/up-8a550c2f92e9866840c19f107a17ca74b58.gif" referrerpolicy="no-referrer"></p> 
<p><span style="color:#7f7f7f">图1 支持产品化配置</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>如图1所示，点击创建工程 > 选择OpenHarmony稳定版本 > 选择想要下载的OpenHarmony源码版本 > 填写工程信息 > 点击确定后开始下载OpenHarmony镜像。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>接着在资源管理器中右键单击 > 选择OpenHarmony > Add new product > 然后在产品创建向导中填写供应商名称，产品名称，继承自开发板名称和产品名称 > 点击确定后会一键创建该产品的目录结构和最小文件集合。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px"><span>最后根据参考链接提供的开发指导，即可开始增量开发。</span></p> </li> 
</ol> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#7f7f7f"><strong><span style="color:#7f7f7f">开发指导：</span></strong></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f">https://gitee.com/openharmony/docs/blob/master/zh-cn/device-dev/subsystems/subsys-build-mini-lite.md#%E8%8A%AF%E7%89%87%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>二、支持芯片基线工程流转</span></span></strong></p> 
<p><span style="color:#333333">芯片基线工程是进行模组或设备开发的基础。</span><span style="color:#333333">以往上游的芯片厂商在适配HarmonyOS Connect后会生成一个基线工程，下游的模组或设备厂商需要手工同步芯片基线工程后才能进一步开发，导致效率降低。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>为了解决上述问题，新版本DevEco Device Tool新增支持芯片基线工程的流转能力。上游芯片厂商在完成HarmonyOS Connect适配后，将代码信息、代码仓路径、资源中心的工具链URL等信息打包到profile文件并上传DP（Device Partner）平台托管。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>下游模组/设备厂商获取profile文件后可以使用DevEco Device Tool<strong>一键导入并自动解析，包括读取芯片定义信息并自动创建芯片对应的目录结构和最小文件集合、读取依赖的编译/烧录工具链信息并从资源中心自动下载、配置repo和git工具并使用repo下载manifest清单中的仓库等，大幅简化了开发步骤</strong>，助力HarmonyOS Connect模组或设备开发效率提升。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>此外，在模组或设备开发完成后，DevEco Device Tool还支持对manifest和profile文件进行重打包，以便上传到DP（Device Partner）平台进行后续托管和流转。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>具体使用方法：</span></strong></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-ef59b2c1440e1daa2773513f1ba5dd2909d.gif" referrerpolicy="no-referrer"></p> 
<p><span style="color:#7f7f7f">图2 基线工程一键导入</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>如图2所示，点击创建工程 >选择HarmonyOS Connect解决方案 >选择下载好的profile文件导入。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>随后点击确定，DevEco Device Tool会自动启动OpenHarmony镜像下载，请耐心等待基线工程下载完成。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>下载完成后参考链接提供的开发指导，即可基于芯片厂商提供的基线工程继续开发产品。</span></p> </li> 
</ol> 
<p><span><span style="color:#7f7f7f"><strong><span>注：</span></strong></span><span style="color:#7f7f7f">在导入profile文件时，如 DevEco Device Tool会自动检测依赖工具是否满足，如果不满足请点击Repo linstallation Guide参考指导操作，主要参考链接里的“前提条件”的5个步骤即可。</span></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#7f7f7f"><strong><span style="color:#7f7f7f">repo installation guide 链接：</span></strong></span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f">https://gitee.com/openharmony/docs/blob/master/zh-cn/device-dev/get-code/sourcecode-acquire.md?utm_source=deveco-device-tool#%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>三、支持一键生成标准设备HDF通用驱动模板</span></span></strong></p> 
<p><span style="color:#333333">HDF（Hardware Driver Foundation）驱动框架，为驱动开发者提供驱动框架能力，包括驱动加载、驱动服务管理和驱动消息机制。</span><span style="color:#333333">以往在进行HDF开发时，开发者需要在不同目录编写makefile文件，hcs文件，c++头文件和源文件，kconfig文件，操作步骤繁琐。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>为了解决上述问题，新版本DevEco Device Tool新增<strong>支持一键生成标准（Standard）系统HDF通用驱动模板</strong>到对应代码目录中，减少新建HDF驱动模板的操作步骤，为驱动开发者提高了开发效率。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>如下表所示，目前只有2种源码类型对应的产品才支持生成HDF，通过HPM导入的发行版源码暂不支持生成HDF。在使用此功能时，请用DevEco Device Tool提供的OpenHarmony稳定版本下载OpenHarmony-v3.1-Release源码，或在OpenHarmony社区下载OpenHarmony master版本的源码使用。</span></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#222222; display:table; font-family:system-ui,-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.544px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:0px; text-align:justify; text-decoration-color:initial; text-decoration-style:initial; text-indent:0px; text-transform:none; white-space:normal; widows:2; width:556px; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px"> 源码类型</p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:8px; margin-right:8px">产品</p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p>OpenHarmony-v3.1-Release</p> <p> </p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> 
    <ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
     <li> <p style="margin-left:0; margin-right:0">ipcamera_hispark_taurus</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">ipcamera_hispark_taurus_linux</p> </li> 
    </ul> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> <p style="margin-left:0; margin-right:0"> </p> <p>OpenHarmony master</p> <p> </p> </td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top"> 
    <ul style="list-style-type:disc; margin-left:8px; margin-right:8px"> 
     <li> <p style="margin-left:0; margin-right:0">ipcamera_hispark_taurus</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">ipcamera_hispark_taurus_linux</p> </li> 
     <li> <p style="margin-left:0; margin-right:0">hispark_taurus_standard</p> </li> 
    </ul> </td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>具体使用方法：</span></strong></p> 
<p><img alt height="481" src="https://oscimg.oschina.net/oscnet/up-e7f196c6d64a6784606ea5964481338dfb1.gif" width="1078" referrerpolicy="no-referrer"></p> 
<p><span style="color:#7f7f7f">图3 生成HDF驱动模板</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:left"><span>下载源码后，选择产品类型，然后点击图3所示工具栏中的HDF > 在HDF的驱动模块中选择蓝色的+号即可创建需要的HDF驱动模板。</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>四、集成QEMU仿真器</span></span></strong></p> 
<p><span style="color:#333333">在嵌入式设备开发过程中，常常遇到代码已开发完成，开发者却因为缺少物理开发板，无法验证编译生成的镜像文件是否能正常运行，也不能进行代码调试和纠错，导致设备开发周期延长，影响项目进度。</span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span>为了解决上述问题，新版本DevEco Device Tool 基于QEMU<strong>提供了开发板的模拟仿真能力，支持arm_virt和mps2-an386两款仿真开发板，能让源码编译后的镜像文件直接运行在仿真器上</strong>（当前只支持OpenHarmony V3.1 Release源码），并提供Native应用的图形显示、可视化UI界面和功能交互能力；此外，<strong>还支持</strong><strong>在开发板上进行应用/内核调试，从而帮助开发者大大减少硬件连接和上板调试的时间</strong>，即使在家也能随时分析软件代码，让设备开发更加便捷高效。 </span></p> 
<p><span style="color:#7f7f7f">图4 仿真开发板使用方法</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>如图4所示，点击导入工程 > 选择工程路径和OpenHarmony源码后点击OK > 选择产品、MCU、开发板以及OpenHarmony版本号后点击打开即可。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>然后点击build进行编译。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>最后点击run开始下载仿真器组件，下载完成后再次点击run按钮，进行镜像传输，镜像传输后即可运行仿真器。</span></p> </li> 
</ol> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#7f7f7f"><strong><span style="color:#7f7f7f">仿真器的调试操作参考官网链接：</span></strong></span></p> 
<p style="color:#333333; margin-left:8px; margin-right:8px; text-align:left"><span style="color:#7f7f7f">https://device.harmonyos.com/cn/docs/documentation/guide/debug_overview-0000001050164998</span></p> 
<p> </p> 
<p style="margin-left:0; margin-right:0"><strong><span><span>五、增强调试能力</span></span></strong></p> 
<p><span style="color:#333333">在开发过程中，调试能力尤为重要，一个好用的调试功能可以帮助开发者事半功倍地完成开发任务。</span><span style="color:#333333">DevEco Device Tool在已有的调试功能上增强了以下调试能力：</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>根据汇编地址查看汇编上下文，提供快速打开反汇编接口、搜索反汇编地址、搜索函数以及支持反汇编和源码之间的快速切换功能。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>支持根据偏移地址计算内存，提供起始地址，偏移地址，长度即可计算得出内存。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>支持内存视图每行按字节排列。</span></p> </li> 
</ol> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><strong><span>具体使用方法：</span></strong></p> 
<p><img alt height="575" src="https://oscimg.oschina.net/oscnet/up-2416ca1c7d75843f42e976f21a47d5c1ddc.gif" width="1079" referrerpolicy="no-referrer"></p> 
<p><span style="color:#7f7f7f">图5 调试使用方法</span></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>如图5所示，点击左下角的“open disassembly view by current function ” > 快速打开反汇编接口 > 将反汇编视图移到右边，方便一起查看源码和反汇编视图。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>点击<span style="color:#333333">左</span>下角的“open disassembly view by address” > 在弹出的搜索框中输入反汇编地址 > 在反汇编视图中可以查找该反汇编地址的上下文。</span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>点击<span style="color:#333333">左</span>下角的“open disassembly view by function name” > 在弹出的搜索框中输入函数 > 在反汇编视图上查找该函数首地址的上下文 </span></p> </li> 
 <li> <p style="margin-left:8px; margin-right:8px; text-align:left"><span>点击的“open memory view” > 在弹出的框中分别输入起始地址、偏移地址和长度，然后点击GO按钮，即可根据偏移地址计算内存 > 点击setting，会出现BYTE SIZE、 GROUP PER ROW和ENDIANESS（大小端选择），页面会按照对应的选择进行显示。</span></p> </li> 
</ol> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#004080"><strong><span style="color:#004080">HUAWEI DevEco Device Tool新功能一览</span></strong></span></p> 
<p><span style="color:#004080"><strong><span style="color:#004080">新增特性:</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span><span>● </span>新增支持自动创建相应的芯片/设备目录结构和最小文件集合，减少创建芯片适配工程手动添加文件夹和文件的操作步骤。</span></p> 
<p style="margin-left:0; margin-right:0"><span>● 新增OpenHarmony稳定版本、OpenHarmony样例下载，HarmonyOS Connect解决方案集成基线工程一键导入。</span></p> 
<p style="margin-left:0; margin-right:0"><span>● 新增支持生成标准设备HDF的通用驱动模板。</span></p> 
<p style="margin-left:0; margin-right:0"><span>● 新增支持arm_virt和mps2-an386两款仿真开发板，支持基于LiteOS-M的内核调试，支持OpenHarmony镜像应用的图形显示。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#004080"><strong><span style="color:#004080">增强特性:</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span><span>● </span></span>提供和OpenHarmony官网样例一致的样例中文名称，修改对应描述增加搜索过滤功能，为所有样例增加使用指导超链接。</p> 
<p style="margin-left:0; margin-right:0"><span>● 调试功能增强：支持根据汇编地址查看、搜索上下文；支持根据偏移地址得到内存；支持内存视图每行按字节排列。</span></p> 
<p style="color:#222222; margin-left:8px; margin-right:8px; text-align:justify"><span style="color:#004080"><strong><span style="color:#004080">修复的问题:</span></strong></span></p> 
<p style="margin-left:0; margin-right:0"><span><span>● </span>修复了创建工程成功后，Ubuntu目录下有工程，但DevEco Device Tool中不显示工程的问题。</span></p> 
<p style="margin-left:0; margin-right:0"><span>● 修复了HPM工程不能正常打开的问题。</span></p> 
<p style="margin-left:0; margin-right:0"><span>● 修复了VSCode在远程模式下无法识别本地PC的端口但能识别Ubuntu端口，以及上传失败的问题。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            