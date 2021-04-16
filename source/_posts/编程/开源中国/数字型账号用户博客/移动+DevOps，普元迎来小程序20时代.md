
---
title: '移动+DevOps，普元迎来小程序2.0时代'
categories: 
 - 编程
 - 开源中国
 - 数字型账号用户博客
headimg: 'https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCawibcnRkfTtrUzowGkPLSSQsN27saTAYF8T1RpfsUCDRXev9C5jL5zw/640?wx_fmt=jpeg'
author: 开源中国
comments: false
date: 2021-04-16 04:11:09
thumbnail: 'https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCawibcnRkfTtrUzowGkPLSSQsN27saTAYF8T1RpfsUCDRXev9C5jL5zw/640?wx_fmt=jpeg'
---

<div>   
<div class="content">
                                                                                                                                                                                        <p style="color:#333333; text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCawibcnRkfTtrUzowGkPLSSQsN27saTAYF8T1RpfsUCDRXev9C5jL5zw/640?wx_fmt=jpeg" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span><strong><span style="color:#888888">​转载本文需注明出处：微信公众号EAWorld，违者必究。</span></strong></span></p> 
<p> </p> 
<p><span style="color:#000000"><strong>前言：</strong></span></p> 
<p> </p> 
<p><span>Primeton® Mobile移动平台是一款集移动开发、运营、运维、管理一体化的智能平台，为客户提供一站式移动解决方案，帮助客户快速高效的构建移动生态，提升企业工作效率和管理模式，加速企业信息化商业模式的创新和变革。本文我们从独立应用的开发入手，跟大家分享一下普元移动平台是如何帮助我们快速构建企业应用。</span></p> 
<p> </p> 
<p><span style="color:#000000"><strong>目录：</strong></span></p> 
<p> </p> 
<p><span>1.开发环境介绍</span></p> 
<p><span>2.神秘的微应用</span></p> 
<p><span>3.丰富的组件</span></p> 
<p><span>4</span><span><span>.</span>基于DevOps继续集成</span></p> 
<p> </p> 
<p><span style="color:#4a94e7">1.开发环境介绍</span></p> 
<p style="color:#333333; text-align:justify"><span>移动平台8.0打开了以往eclipse平台的枷锁，全面拥抱了主流的VSCode编辑器，包括支持实用的cli命令行支持、及优秀的跨平台开发框架ReactNative。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCUEtjmWN1Sv4yMjc29uic0KDicTF6uGR7m6icoTLHLfTSh4eDsnicyjRmhA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>移动开发平台提供了VSCode插件，并发布到官方应用市场。支持Primeton Mobile开发工具的安装，及项目创建、编译、调试、打包等命令，并提供了详细的文档及动画演示。快速的迭代开发使我们紧跟VSCode的更新，提供更方便快捷的开发体验。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCmDsliamqDKM4OKPBLd5AXe4hcnLvMBygtlKOktrVf5B3sKn95UUGshA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oC5EABvJJ1YvLyvdbPMgLIJag81uLJE90wcnPXINXzVvMeHJwwwmHlsw/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>简单执行命令npm install -g mobile-dev-cli即可安装移动开发平台cli命令行工具，工具包会跟随移动产品版本发布并持续更新。命令行提供了与VSCode插件同样的一套功能，专门为持续集成打造，无需安装VSCode也可以享受移动平台所有功能。同时提供pmobile check命令，一键检查环境变量，为安装开发环境保驾护航。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCJRk381hh9qZ3G6pBmvLgiaoVtU1ameI3DHcs9lCsGlzoPbv73icS53IA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>devtools是平台提供的完整的工具包，包括Android、iOS平台编译打包，组件扩展、调试基座配置等功能。开发者可以在/android、/ios目录下自行进行扩展开发，并重新打包调试基座或生产App。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oC4Qv3hiaMicNwhH2ZSXI2QLx9srsz5PtLXz00TSWtLQRQKWDMFZEnsicdw/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span style="color:#4a94e7">2.神秘的微应用</span></p> 
<p><span>说到微应用大家很陌生，但小程序肯定都知道，而且是各种大厂的小程序，普元也不例外。早在2016年11月，普元移动开发平台7.1GA发布的时候就已经全面支持了小程序，并在某国有通信龙头企业中落地使用。当时平台就全面支持微应用开发、调试、测试、打包等功能，并开放普元微应用管理后台，提供微应用的上传、审核、上线等功能，同时支持手机客户端中应用商店能力，包括获取应用列表、应用下载安装、检查更新、热更新等。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCYialpQkHcw6LUsTcaj6tIUT2iaJL14wcucptrTzdlRic60GDCAkXialLaA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span>普元微应用1.0</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oC3YExssBljB0FiasBmdia0icDhFIWL42iaQmAJsmxCxFFsBjG3LeX6vCawQ/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span>普元微应用2.0</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCqLdFDYrqIgDzBDWbMicTOkW7RGDKy3OmUedoZyTib3nVQYWR6xsea7Vg/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>随着Primeton® Mobile移动平台8.0GA版本于上周发布，普元的微应用跨入了2.0版本。新版本的微应用支持共四种应用类型：ReactNative微应用、Html5在线应用、Html5离线应用、原生应用，后续会持续迭代支持Cordova应用、Flutter应用等。微应用的UI也做了统一的管理，风格统一的标题栏、返回关闭按钮、底部菜单等。新版本微应用管理平台也做了大量升级，在兼容老版本所有功能的同时，优化了微应用授权、内测、运营等功能，也提供了微应用下载次数、打开次数、使用时长等数据的统计和展示。</span></p> 
<p style="color:#333333; text-align:justify"><span>普元不但是小程序浪潮中的参与者，也是小程序国际和国内标准的制定者。2020年7月30日，《Standard for Mini-program Architecture and Technical Requirements》（IEEE P2858）标准启动会在北京环球金融中心成功召开，普元信息移动产品线作为参赛单位的一员，为完善和开展国内标准建设、推进扩大市场化应用和促进小程序生态发展做出了贡献。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCuhsgxddlIQQrnYmJJPAoT1mHic5iauB3bZDSTvRj3QwBtfFg177LepkQ/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>插句题外话，移动运营管理平台还支持门户应用的消息推送、日志分析、API网关、安全审计、门户楼层的配置、千人千面等功能，在此不做赘述，感兴趣的可以去售后申请试用。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCPoN3tOCmsawOaJ0mrWtqF8fEmiaUZfg5UKiakTzhV80GJw3vuEWEiaZGQ/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>普元移动平台同时提供了大量行业App的模板，包括电商模板（仿京东App），银行模板（仿招行App）等，这些模板开箱即用，无需任何配置，UI方面也是参考行业龙头企业App的设计，满足用户快速开发、快速上线的需求。当然，你也可以创建一个空白RN项目，从零开始开发，体验原汁原味的ReactNative开发。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCicto7ciakVD2AVA8nA5OjHjyRrO0Kcy9QibiaP552Nnhb7kdEkZjQdpStw/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>普元微应用与ReactNative原生应用不同，它将开发与打包分离开来。微应用的开发环境只关心RN开发，而把原生部分分离在项目之外，所以该目录结构对于只做RN开发的人来说会更加合理和便捷。微应用的代码部分在src下，配置文件在config下，打包产物在output下。开发者在开发阶段只需关注src下代码部分，专注开发业务逻辑，打包则交给平台完成。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCWf2g4tnicLlibhaHoBNEjZ3I2tK0gdWXM1Co3awC42016sUsWc0fAicdA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span>VSCode不仅提供了模板，还提供了调试微应用的能力，点击右上角的小按钮即可快速启动调试服务。启动调试服务后，手机端通过调试客户端就能够实时预览代码效果，进行开发了。当然，如果没有安装VSCode，也可以通过全局cli命令，直接在命令行中执行pmobile start启动调试服务。VSCode插件支持Windows、Mac电脑上对Android、iOS的调试。调试服务支持调试期微应用编译并下载到手机，也集成了改造过后的ReactNative的调试服务，让我们能够以原生ReactNative的调试体验开发普元微应用。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCZjdicuSVNiaq2LZbTAEp153O5GjZNURkl5yXuicEdL7gFJFXlEBicYk8ibg/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>你可以通过扫码下载最新的调试客户端，目前我们支持调试客户端和调试服务在同网段的代码调试（Android可以通过adb端口转发实现无网络调试），同时Android和iOS也都支持模拟器安装调试，为部分企业的内网调试提供支持。</span></p> 
<p style="color:#333333; text-align:justify"><span>调试客户端不但支持代码开发预览，还支持在VSCode编辑器内断点调试、查看布局属性、查看应用网络请求等功能，还可以在非开发环境（未连接调试服务）下进行微应用的离线运行。这都得益于我们高度定制化的分包机制，在此不做展开，感兴趣可以持续关注EAWorld公众号和微课堂。</span></p> 
<p><span style="color:#4a94e7">3.丰富的组件</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCKCIvrE370VeYVPSGng47TPiaVmn0c5yS1njF6rYcblMhzficZ2l9JNzA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>在移动8.0GA产品中，我们提供了60多个组件，可以在配置打包信息时看到并勾选使用。组件包括ReactNative最常用到的导航组件、UI组件、ReactNativeCommunity社区提供的优秀的组件等，还有二维码、视频、音频、H5等支持。企业也可以将自己集成的组件发布到组件仓库中，形成组件资产的积累。</span></p> 
<p style="color:#333333; text-align:justify"><span>在配置打包页面，我们可以直接勾选项目使用的组件，如果有参数配置可以直接在右侧输入（比如微信appId等）。勾选时，有依赖的组件也会自动勾选，无需用户特别关注。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oC2FHUqkJyyB1Lia1A6ZAzeDBHLC5jBhN7Od1uzcfLbLSgHvO5vFb2a7A/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>标准组件是基于普元移动平台，开发和编译过程中可插拔式的UI和功能库。当标准产品提供的API无法满足业务需求时，需要扩展组件来实现。扩展组件可以直接在开发环境devtools中直接开发，也可以使用pmobile link命令快速集成ReactNative三方组件，link命令执行后，脚本会修改/android下的项目依赖和ReactPackage的添加，/ios下pod文件增加依赖并pod install，/js下增加对组件的引用，这样打包出来的基座就可以直接使用这个组件了。</span></p> 
<p><span style="color:#4a94e7">4.基于DevOps继续集成</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCaUibQACiaFrrpiaD8zDOEP53eMwfpQpPS8NrTcWngS7TM58V5asMPrhbA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; text-align:justify"><span>平台提供了丰富的打包参数，并提供可视化页面，可以配置应用首页、版本号、欢迎页、App服务地址等，同时iOS支持打包app-store、enterprise、ad-hoc三种模式，并支持模拟器、安全通道、白名单等配置。组件也可以通过简单的勾选使用，无需重复开发，就能简单使用提供的60余组件。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCuR7dgN9PmFic2iaWbJ14JWyg3drjibDVd4z4x3fayRrGmGHRMefx3A6iaA/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span>对于移动类的应用，目前我们支持安卓应用的构建，首先是拉取代码，可以从Git库拉取，也可以从svn拉取，接着初始化打包环境并执行打包脚本，完成后选择发布到nexus或微应用的应用商店中。</span></p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCQGoTAwVXKK6eaTowEdKznLkEqpJQkyO3hDkE6ONWVANQNibz5Iap6bg/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p><span>普元移动门户管理平台不但提供了移动应用的更新、发布等功能，还提供了应用的上传、下载、二维码下载等能力。上传功能和DevOps打通，在编译成功后直接发布到应用商店中，开发测试人员可以直接扫码下载最新的App，实现开发测试流程的闭环。</span></p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWJs6J6xjjjqQibr1qATy1oCHneLIpnVB70nep3CDuzicJNfjKRb9HicwY9sdEQNkDYuJ14kUVh7AqyA/640?wx_fmt=png" width="538" referrerpolicy="no-referrer"></p> 
<p><span>目前移动开发平台8.0GA版本已经在内部使用，企业内部应用如会议室预定、工时填报也在紧锣密鼓的开发中，为了方便使用DevOps，也开发了DevOps移动App。可以在手机端查看DevOps中的任务、构建、发布、工单，同时构建状态也可以在手机端显示，更酷的是可以在手机端直接执行构建。例如第三张图，我在DevOps移动App中构建DevOps移动App（禁止套娃）。</span></p> 
<p><span>总的来说，普元移动开发平台对微应用做了大量的优化，支持了四种微应用类型，提供了丰富的组件供开发人员选择。同时提供了DevOps移动App，支持在移动端进行编译打包发布等。新版本全面支持VSCode编辑器，同时提供cli命令行工具，为开发人员提供了方便快捷的开发环境，助力企业快速构建移动应用。</span></p> 
<p> </p> 
<p style="color:#3e3e3e; text-align:justify"><img align="left" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWaNBdc2NWGRMLOZT5ntKc9W2xe4xicKBJXrXzIm2N23pMz7iaLMsMgjQlPCxtppVfegtAuxFQ4UEvA/640?wx_fmt=png" width="124" referrerpolicy="no-referrer"><span><strong>关于作者</strong><span>：</span>明月，现任普元移动团队资深开发工程师，长期致力于IT技术研究，产品设计和开发等工作，擅长Java、NodeJs、ReactNative等领域技术。先后参加深圳登、太平洋保险等移动项目的实施，参与Mobile 8.0移动平台的设计开发工作。</span></p> 
<p style="color:#3e3e3e; text-align:justify"> </p> 
<p style="color:#3e3e3e; text-align:justify"><img align="left" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWaNBdc2NWGRMLOZT5ntKc9qSzg9vyORia2VmUhhfsXx4Q9xBBSFIPDEF7y4YKDpy1uG37WliaqCBbw/640?wx_fmt=png" width="127" referrerpolicy="no-referrer"><strong><span>关于EAWorld</span></strong><span>：微服务，DevOps，数据治理，移动架构原创技术分享。<strong>长按二维码关注！</strong></span></p>
                                        </div>
                                      
</div>
            