
---
title: 'DevEco Studio 2.1 正式发布，HarmonyOS 的配套 IDE'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e6474f0d8724e5a7da68c912585dd920858.png'
author: 开源中国
comments: false
date: Fri, 18 Jun 2021 17:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e6474f0d8724e5a7da68c912585dd920858.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>DevEco Studio 2.1 发布已有一段时间，因为是正式版本，所以在此同步一下。</p> 
<p>经过多个 Beta 测试版本的迭代，DevEco Studio 2.1 在6月2日发布了首个正式版本，下面是更新说明。</p> 
<h1>新增特性</h1> 
<h2>一、新增跨设备工程模板</h2> 
<p><strong>为了满足应用在多设备上运行的开发需求，DevEco Studio 2.1 Release在原有单设备工程模板的基础上，新增了11个跨设备工程模板。</strong></p> 
<p>开发者可根据工程向导，依次挑选模板和设备类型，轻松创建跨设备工程，自动生成示例代码和相关资源。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e6474f0d8724e5a7da68c912585dd920858.png" referrerpolicy="no-referrer"></p> 
<h2>二、新增支持原子化服务开发</h2> 
<p>原子化服务（Atomic Service）是HarmonyOS提供的一种面向未来的应用程序形态，相对于传统的需安装的应用形态，免安装的原子化服务既能满足用户在不同场景、不同设备上的使用需求，又能给应用提供更丰富的入口、更精准的分发。</p> 
<p><strong>DevEco Studio 2.1 Release新增支持原子化服务（Atomic Service）开发。开发者可在选择工程模板后，快速创建原子化服务工程，并进行后续的代码开发、编译、调试等操作。</strong></p> 
<p>温馨提示，新版本中工程创建向导功能发生了较大变化，具体体现在：</p> 
<ol> 
 <li>历史版本中，开发者需先选择设备，再选择工程模板。但在最新版本中，开发者需先选择工程模板，再选择支持的设备类型。</li> 
 <li>创建工程时，项目类型新增了“Service”选项，可用来创建原子化服务工程。</li> 
 <li>如果创建的是原子化服务工程，可通过点击“Show in Service Center ”，来使得此服务可在设备端的服务中心被轻松查找到。</li> 
</ol> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e9f17a3b0616dd5f56f33810784133c845c.png" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-589e90474baa36d465178d497159f1bc558.png" referrerpolicy="no-referrer"></p> 
<h2>三、新增支持路由器设备</h2> 
<p><strong>DevEco Studio 2.1 Release新增支持路由器（Router）设备。</strong><strong>开发者可通过DevEco Studio中的路由器单设备工程模板，使用JS语言，快速开发能运行在路由器设备上的应用。</strong></p> 
<p>至此，DevEco Studio已支持手机(Phone)、平板(Tablet)、车机(Car)、智慧屏(TV)、智能穿戴(Wearable)、轻量级智能穿戴(Lite Wearable)、智慧视觉 (Smart Vision)和路由器（Router）八种设备。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d3e1d63b79e139346b8ee325a6ea5dae73a.png" referrerpolicy="no-referrer"></p> 
<h2>四、支持 Sample 工程导入</h2> 
<p>HarmonyOS Sample是HarmonyOS的示例应用程序，开发者们可以通过Sample来快速了解如何使用不同的API构建应用程序、创建项目。</p> 
<p>DevEco Studio 2.1 Release支持Sample工程导入。开发者通过“Import HarmonyOS Sample”菜单界面将Sample工程自动导入到DevEco Studio中，即可直接查看Sample工程代码。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-83d934f1618ec65f2e27f514ec191888f4c.png" referrerpolicy="no-referrer"></p> 
<h2>五、新增分布式模拟器</h2> 
<p>DevEco Studio 2.1 Release新增了分布式模拟器（Super device）。</p> 
<p>分布式模拟器是远程模拟器（Remote Emulator）中的一种，需要登录授权，且每次的使用时长为1小时，到期后会自动释放，释放后可重新申请。开发者可使用分布式模拟器来测试应用的分布式功能，例如：应用在不同设备间流转的功能。本次DevEco Studio 2.1 Release版本的分布式模拟器，支持部署在“Phone+Phone”和“Phone+Tablet”上的分布式应用测试。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-cbf7e534c1d19f33777852ad441942b7d06.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>注：DevEco Studio 2.1 Release提供分布式模拟器功能处于实验阶段，开发者需在“Settings-DevEco Labs”页面中勾选“Enable Super device”按钮尝鲜。在使用过程中碰到的问题，会在后续版本中迭代优化。</p> 
</blockquote> 
<p>除了以上几项突破，DevEco Studio 2.1 Release在某些已有特性上也做了增强，同时修复了一些遗留问题，具体优化细节如下：</p> 
<h1>增强特性</h1> 
<ul> 
 <li>HarmonyOS SDK更新至2.1.1.21版本，Stage为Release。同时优化了HarmonyOS SDK的下载，第一次安装DevEco Studio，默认会同时下载Java SDK、JS SDK、Toolchains、Previewer。</li> 
 <li>应用签名能力增强： 
  <ul> 
   <li>支持调测应用自动化签名。</li> 
   <li>支持通过配置文件方式存储应用签名信息。</li> 
  </ul> </li> 
 <li>Java编辑器能力增强，通过集成HuaweiCloud SmartAssist提供更智能的代码补齐能力。</li> 
 <li>预览器能力增强，请将HarmonyOS SDK更新至最新版本。 
  <ul> 
   <li>支持限定词目录下的xml文件预览。</li> 
   <li>优化预览器图像传输、实时预览性能。</li> 
  </ul> </li> 
 <li>服务卡片（Service Widget）增强，支持Wearable设备的卡片开发，并新增多个卡片模板。</li> 
 <li>编译构建的性能优化，提升Hap/App的编译构建速度。</li> 
 <li>Har支持C++共享库构建和使用。</li> 
 <li>优化HiLog日志输出结果的显示效果，并支持过滤筛选。</li> 
</ul> 
<h1>解决的问题</h1> 
<ul> 
 <li>解决了graphic目录下shape和vector无法自动联想的问题。</li> 
 <li>解决了entry和feature模块无法多层级引用har资源的问题。</li> 
 <li>解决了webview组件在模拟器上不能显示的问题。</li> 
 <li>解决了Phone设备没有C/C++工程模板的问题。</li> 
 <li>解决了预览器不能进行横竖屏切换的问题。</li> 
 <li>解决了预览器不支持多语言（除中文和英文外）的问题。</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdevelop%2Fdeveco-studio" target="_blank"><strong>下载地址</strong></a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdocs%2Fdocumentation%2Fdoc-guides%2Ftools_overview-0000001053582387" target="_blank"><strong>用户指南</strong></a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdocs%2Fdocumentation%2Fdoc-releases%2Frelease_notes-0000001057597449" target="_blank"><strong>版本说明</strong></a></p>
                                        </div>
                                      
</div>
            