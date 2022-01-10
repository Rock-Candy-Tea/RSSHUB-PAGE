
---
title: 'OpenHarmony 3.1 Beta 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-63ec9e81cce5db6bb10fbac5deedea4391f.png'
author: 开源中国
comments: false
date: Mon, 10 Jan 2022 07:39:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-63ec9e81cce5db6bb10fbac5deedea4391f.png'
---

<div>   
<div class="content">
                                                                                            <p>OpenAtom 社区已于 12 月 31 日发布了 OpenHarmony-v3.1-Beta 版本。</p> 
<p>新版本在 OpenHarmony 3.0 LTS 的基础上，更新支持了以下能力：</p> 
<p><strong><span style="color:#595959">①标准系统 OS 基础能力增强：</span></strong><span style="color:#595959">内核提升 CMA 利用率特性、图形新增支持 RenderService 渲染后端引擎、短距离通信支持 STA（Station）和 SoftAP 基础特性、支持地磁场的算法接口、传感器驱动模型能力增强、支持应用帐号信息查询和订阅等、全球化特性支持、编译构建支持统一的构建模板、编译运行时提供 Windows/MacOS/Linux 的前端编译工具链、JS 运行时支持预览器、新增支持 JSON 处理、Eventbus、Vcard、Protobuf、RxJS、LibphoneNumber 等 6 个 JS 三方库、新增时间时区管理、DFX 新增支持 HiSysEvent 部件提供查询和订阅接口。</span></p> 
<p><strong><span style="color:#595959">②标准系统分布式能力增强：</span></strong><span style="color:#595959">包括新增支持分布式 DeviceProfile 特性、分布式数据管理支持跨设备同步和订阅、分布式软总线支持网络切换组网、分布式文件系统支持 Statfs API 能力等。</span></p> 
<p><strong><span style="color:#595959">③标准系统应用程序框架能力增强：</span></strong><span style="color:#595959">新增 ArkUI 自定义绘制能力和 Lottie 动画能力、新增包管理探秘隐式查询和多 hap 包安装、事件通知支持权限管理、设置通知振动、通知声音设置和查询、通知免打扰、会话类通知等。</span></p> 
<p><strong><span style="color:#595959">④标准系统应用能力增强：</span></strong><span style="color:#595959">输入法应用支持文本输入和横屏下布局显示、短信应用信息管理、联系人应用通话记录和拨号盘显示、设置应用更多设置项。</span></p> 
<p><strong><span style="color:#595959">⑤轻量系统能力增强：</span></strong><span style="color:#595959">HiStreamer 轻量级支持可定制的媒体管线框架、Linux 版本 init 支持热插拔、OS 轻内核 & 驱动启动优化、快速启动能力支持。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-63ec9e81cce5db6bb10fbac5deedea4391f.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0px; margin-right:0px">源码获取</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><span style="color:#595959">开发者现可通过 repo + ssh 下载（需注册公钥）或者通过 repo + https 下载源码，芯片及开发板适配状态请参考官方 SIG-Devboard 信息。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#595959">方式一（推荐）：</span></strong><span style="color:#595959">通过 repo + ssh 下载（需注册公钥，请参考码云帮助中心）。</span></p> 
<pre><code>repo init -u git@gitee.com:openharmony/manifest.git -b refs/tags/OpenHarmony-v3.1-Beta --no-repo-verify
repo sync -c
repo forall -c 'git lfs pull'</code></pre> 
<p><strong><span style="color:#595959">方式二：</span></strong><span style="color:#595959">通过 repo + https 下载。</span></p> 
<pre><code>repo init -u https://gitee.com/openharmony/manifest.git -b refs/tags/OpenHarmony-v3.1-Beta --no-repo-verify
repo sync -c
repo forall -c 'git lfs pull'</code></pre> 
<p><span style="color:#595959">据公开资料显示，OpenHarmony 开源项目是由开放原子开源基金会孵化及运营的开源项目，由开放原子开源基金会 OpenHarmony 项目群工作委员会负责运作。</span></p> 
<p><span style="color:#595959">OpenHarmony整体遵从分层设计，从下向上依次为：内核层、系统服务层、框架层和应用层。</span></p> 
<p><span style="color:#595959">系统功能按照“系统 > 子系统 > 组件”逐级展开，在多设备部署场景下，支持根据实际需求裁剪某些非必要的组件。</span></p> 
<p><span style="color:#595959">OpenHarmony技术架构如下所示：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-d04dfab90ae6af61c46a4e3d591718e8d4e.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">OpenHarmony 支持如下几种系统类型：</p> 
<p><strong><span style="color:#595959">轻量系统（mini system）：</span></strong><span style="color:#595959">面向 MCU 类处理器例如 Arm Cortex-M、RISC-V 32 位的设备，硬件资源极其有限，支持的设备最小内存为 128KiB，可以提供多种轻量级网络协议，轻量级的图形框架，以及丰富的 IOT 总线读写部件等。可支撑的产品如智能家居领域的连接类模组、传感器设备、穿戴类设备等。</span></p> 
<p><strong><span style="color:#595959">小型系统（small system）：</span></strong><span style="color:#595959">面向应用处理器例如 Arm Cortex-A 的设备，支持的设备最小内存为 1MiB，可以提供更高的安全能力、标准的图形框架、视频编解码的多媒体能力。可支撑的产品如智能家居领域的 IP Camera、电子猫眼、路由器以及智慧出行域的行车记录仪等。</span></p> 
<p><strong><span style="color:#595959">标准系统（standard system）：</span></strong><span style="color:#595959">面向应用处理器例如 Arm Cortex-A 的设备，支持的设备最小内存为 128MiB，可以提供增强的交互能力、3D GPU 以及硬件合成能力、更多控件以及动效更丰富的图形能力、完整的应用框架。可支撑的产品如高端的冰箱显示屏。</span></p> 
<p><a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/release-notes/OpenHarmony-v3.1-beta.md#openharmony-31-beta">更多 OpenHarmony 3.1 Beta 更新内容请查看发布说明</a>。</p>
                                        </div>
                                      
</div>
            