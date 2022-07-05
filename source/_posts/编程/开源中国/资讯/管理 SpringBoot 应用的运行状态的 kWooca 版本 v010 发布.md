
---
title: '管理 SpringBoot 应用的运行状态的 kWooca 版本 v0.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8805'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 19:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8805'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">kWooca 是一款用于管理 SpringBoot 应用运行状态的软件。开发该软件的初衷是为了让SpringBoot（或Spring Cloud）应用的开发者们可以更好的在开发工作站上运行相应的应用，因为在SpringBoot(或Spring Cloud)应用开发过程中通常需要同时运行多个SpringBoot应用程序，开发人员不得不需要通过命令行或IDE来运行这些程序，他们也经常需要在各个Shell窗口（Cmd窗口）中来回切换，甚是麻烦。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Wooca的出现，将这些应用统一在一个窗口中进行处理，同时，可以根据应用本身的特点，进行相应的参数配置，达到更好的配置管理的过程。在SpringBoot应用运行过程中，还可以通过Wooca来进行日志、CPU、内存、IO、网络吞吐等多方面的性能指标监控，及时的了解SpringBoot应用的运行状态。Wooca解放了开发人员对Shell/Cmd窗口的依赖，更加集成化的将SpringBoot/Cloud应用捆绑在一起，并对这些应该的启动参数进行统一管理，Wooca提供了一些更加友好的方式来管理这些参数，防止开发人员随意使用这些参数，而造成一些意想不到的缺陷出来。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">软件所需要的依赖库及软件</h3> 
<ol> 
 <li>wxWidget 5.3</li> 
 <li>Visual Studio 2017以及以上版本，支持C++，且提供了至少是Windows 10的SDK。</li> 
 <li>cURL</li> 
 <li>libzip</li> 
 <li>OpenSSL</li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">为了简化使用，项目源文件中提供了具体的安装包：<span> </span><a href="https://gitee.com/poethxp/kwooca/raw/master/release/kWooka.zip">https://gitee.com/poethxp/kwooca/raw/master/release/kWooka.zip</a><span> </span>大家可以直接下载并运行。绿色，无须安装其它依赖。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">版本0.1.0 基础功能说明</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Wooca目前发布出来的版本是0.1.0。该版本实现了对Wooca的基础设想，也就是对SpringBoot应用的运行状态的管理。主要功能如下：</p> 
<ul> 
 <li>创建Wooca项目，选择一个空白的目录，即可创建一个Wooca项目，Wooca会在该目录下建立一个wooka.json的文件，以此表示该目录是一个Wooca项目的工作目录。</li> 
 <li>打开Wooca项目，选择一个包括了wooca.json文件的工作目录，即可进行打开。打开项目后，会将该项目所包含的所有的SpringBoot应用展示在软件的左侧列表中。</li> 
 <li>添加SpringBoot应用到项目，创建或打开项目后，可以通过列表上方的按钮来选择SpringBoot Fat Jar的方式来建立应用，Wooca会读取Jar中的Metadata内容，来生成对应的名称以及版本号等。</li> 
 <li>运行一个SpringBoot应用，双击选择应用列表中某个应用，点击启动按钮可以启动一个应用。</li> 
 <li>停止一个SpringBoot应用，双击选择应用列表中某个应用，如果该应用正在运行中，点击停止按钮可以停止一个应用。</li> 
 <li>删除一个SpringBoot应用，双击选择应用列表中某个应用，点击删除应用的按钮，可以将该应用删除。</li> 
 <li>启动项目中全部应用，打开Wooca项目后，可以使用工具栏中“全部启动”来启动全部的SpringBoot应用。</li> 
 <li>停止项目中全部应用，Wooca中应用运行后，可以使用工具栏中“全部停止”来停止全部正在运行的SpringBoot应用。</li> 
 <li>查看日志，首先是在Wooca项目列表中，双击你要查看的日志的应用，然后在右侧的区域中选择“日志”选项卡。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"> </p> 
<ul> 
 <li>查看性能指标，首先是在Wooca项目列表中，双击你要查看的性能的应用，然后在右侧的区域中选择“性能监控”选项卡。可以通过界面来查看该应用的CPU使用率、内存使用率、磁盘IO、网络吞吐量、线程数变化、句柄数变化。</li> 
</ul> 
<ul> 
 <li>Wooca项目的全局配置，打开Wooca项目后，可以通过工具栏中的“项目属性”来对项目的全局属性进行设置，如全局的JDK HOME、全局的环境变量、全局的Java应用启动参数等。</li> 
 <li>应用的启动参数配置，双击选择应用列表中某个应用，再选择右侧区域的“配置”选项卡，可以对JVM参数、以及应用的配置参数进行调整，如果全局配置中有相同的配置，应用的配置会覆盖全局配置。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"> </p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">运行环境</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Wooca是一个独立免安装的绿色软件，因此，它的体积也就会大一点。同时，Wooca是基于Windows 10的基础进行开发的，采用了wxWidgets 3.1.5进行界面的开发。Wooca可以确保在Windows 10及其以上版本上运行。 Windows 10的用户请直接下载kWooka.exe并直接运行即可。</p> 
<p> </p>
                                        </div>
                                      
</div>
            