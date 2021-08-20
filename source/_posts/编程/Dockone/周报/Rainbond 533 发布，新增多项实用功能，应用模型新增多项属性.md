
---
title: 'Rainbond 5.3.3 发布，新增多项实用功能，应用模型新增多项属性'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/rainbondComponentStatus.png'
author: Dockone
comments: false
date: 2021-08-20 03:07:57
thumbnail: 'https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/rainbondComponentStatus.png'
---

<div>   
<br><blockquote><br> <a href="https://github.com/goodrain/rainbond">Rainbond </a>是云原生且易用的应用管理平台。云原生应用交付的最佳实践。专注于以应用为中心的理念，赋能企业搭建云原生开发云、云原生交付云。<br>
  <br>
  <br> <strong>对于企业：</strong> Rainbond 是开箱即用的云原生平台，借助 Rainbond 可以快速完成企业研发和交付体系的云原生转型。<br>
  <br>
  <br> <strong>对于开发者：</strong> 基于 Rainbond 开发、测试和运维企业业务应用，开箱即用的获得全方位的云原生技术能力。包括但不仅限于持续集成、服务治理、架构支撑、多维度应用观测、流量管理。<br>
  <br>
  <br> <strong>对于项目交付：</strong> 基于 Rainbond 搭建产品版本化管理体系，搭建标准化客户交付环境，使传统的交付流程可以自动化、简单化和可管理。</blockquote>Rainbond 5.3.3 版本来了，本次发布的版本我们主要以用户实际需求为导向进行优化，在过去的一些实践中，我们发现，对于复杂的业务组件，部分资源的配置需要个性化配置，这就对我们平台使用的灵活性提出了更高的要求。因此 5.3.3 版本我们主要以配置的灵活性为主要迭代方向。<br>
<br>在一些开发场景中，用户机器可能是高内存型或高 CPU 型，此时用户机器资源往往得不到充分利用，因此现在我们提供了组件 CPU 设置的能力，用户可以根据自己需求个性化配置资源。其次，对于一些配置文件，用户除了配置文件相关内容外，也有配置其权限的需求，现在这些需求都可以得到满足。<br>
<br><h3>主要功能点解读：</h3><h4>1. 支持实时查看 Rainbond 自身组件的状态和初始化进度</h4>在该版本以前，我们在初始化 Rainbond 集群时，整体对用户是不可见的，相当于一个黑盒，用户出现问题，很难及时定位。现在我们在初始化 Rainbond 集群时，给出了集群的 pod 信息，用户可以通过可视化界面，直接了解到初始化集群需要多少组件，目前已经完成的组件数。还可点击组件，查看组件的事件信息。使用户能更直观的了解整个过程和快速定位问题。效果如下图所示：<br>
<img src="https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/rainbondComponentStatus.png" alt="rainbondComponentStatus.png" referrerpolicy="no-referrer"><br>
<br><h4>2. 支持组件配置文件的权限设置</h4>在之前的版本中，为某个组件挂载配置文件时，默认的权限为 0777 ，但是有些配置文件有权限要求，比如my.cnf，0777 会被忽略，因此在 5.3.3 版本中，支持为挂载的配置文件设置一个权限，用于解决该类问题。<br>
<br><img src="https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/configfilePermSetting.gif" alt="configfilePermSetting.gif" referrerpolicy="no-referrer"><br>
<br><h4>3. 支持组件的CPU设置</h4>在之前，我们只支持了组件的内存设置，CPU 通过算法得出。但这样有以下几个问题：<br>
<ul><li>部分业务由于CPU资源分配过少，运行缓慢。出现问题甚至难以排查。</li><li>在部分开发环境中，用户想自己手动指定相应的 CPU ，也难以操作。</li></ul><br>
<br>因此我们现在支持了自己手动设置组件的 CPU 和内存，且 CPU 和内存资源都可设置为不限制，给用户提供更灵活的使用方式。<br>
<img src="https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/setCPU.gif" alt="setCPU.gif" referrerpolicy="no-referrer"><br>
<br><h4>4. 第三方组件的重构</h4>为了逐步适配 OAM 应用规范，提升 Rainbond 的可扩展性。在之前发布的 5.3.1 版本中我们基于 <a href="https://github.com/oam-dev/spec">OAM规范</a>，重新实现了第三方组件类型，定义了 ThirdComponent 作为第一个 ComponentDefinition，并在产品中实现对ComponentDefinition 的基础管理机制。此次我们基于 ComponentDefinition 定义重新实现了第三方组件的静态配置和 API 配置实例类型。现在第三方组件已支持添加多个端口，并支持对应端口进行绑定。下面我对此次第三方组件的功能点做个简要说明。<br>
<br>假如现在你的第三方组件只开启了 80 端口，此时该组件有以下两个实例 10.10.10.10:80 ，10.10.10.11:5000<br>
<ul><li><br>支持单端口映射到不同端口的endpoints<br>
<br>对于第三方组件，只开通一个端口，添加多个实例且多个实例端口不同时，那么可以通过开通的端口轮询访问到该组件下的所有实例。<br>
<br>参考上述前提，那么此时你访问第三方组件的 80 端口，实际是会轮询访问这两个实例  10.10.10.10:80 ，10.10.10.11:5000</li><li><br>添加多个端口，多个端口的绑定关系<br>
<br>此时为第三方组件新建端口 5000 ，那么对应的端口将会与实例进行绑定，此时访问第三方组件的 80 端口，将只会访问到实例  10.10.10.10:80 ，访问 5000 端口，也只会访问到实例 10.10.10.11:5000。</li></ul><br>
<br><img src="https://cors.zfour.workers.dev/?http://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/3rdComponentsRestructure.gif" alt="3rdComponentsRestructure.gif" referrerpolicy="no-referrer"><br>
<br><h4>5. 应用模版的变更</h4>在 5.3.3 版本中，我们更改了应用模版的元数据模型，支持了更多组件属性的发布。如组件的 CPU 设置、组件特性、组件网关策略、配置文件权限的发布与安装等。其次，基于元数据模型的变更，我们在导出 RAM 规范的应用时，也支持了应用 logo 和版本信息的导出，现在，你可以更好的导入应用并获得该应用的版本信息。<br>
<br><h4>6.  支持组件的容器日志可以单独查看</h4>在以往的版本中，一个组件下有多个容器时，多个容器的日志均输出到日志页面，难以区分。在 5.3.3 版本中，这不再是问题，5.3.3 版本中支持单独查看各容器的日志，你只需在组件日志页面选择你需要查看的容器，即可快速获取到你关心的信息。<br>
<br><h3>详细变更点：</h3><h3>新增功能</h3><ul><li><br>【安装】<strong>支持查询Ranbond组件的状态信息和安装进度；</strong></li><li><br>【应用管理】<strong>支持网关访问策略的发布与安装；</strong> </li><li><br>【组件管理】<strong>支持配置文件设置文件权限；</strong></li><li><br>【组件管理】<strong>支持设置组件和插件的CPU；</strong></li><li><br>【组件管理】<strong>支持查看组件内各容器的日志；</strong></li><li><br>【组件库管理】<strong>支持导入导出应用模版的logo和版本信息；</strong></li><li><br>【第三方组件】<strong>支持第三方组件添加多个端口；</strong></li><li><br>【第三方组件】<strong>支持单端口映射到不同端口的endpoints；</strong></li></ul><br>
<br><h3>优化功能</h3><ul><li><br>【性能】<strong>缓存企业级统计数据，提升首页展示速度；</strong></li><li><br>【存储】<strong>自动清理备份恢复和导入时产生的缓存数据；</strong></li><li><br>【稳定性】<strong>升级底层ingress版本；</strong></li><li><br>【日志】<strong>优化allinone部署的控制台日志持续输出无法连接redis的问题；</strong></li><li><br>【日志】<strong>优化导入大体积模版时rbd-chaos的日志提示</strong>；</li></ul><br>
<br><h3>BUG 修复</h3><ul><li>【安装】<strong>修复集群安装驱动服务崩溃的问题；</strong></li><li>【安装】<strong>修复同名称集群,重新安装失败的问题；</strong></li><li>【安装】<strong>修复初始化Rainbond集群操作未实现幂等的问题；</strong></li><li>【网关】<strong>修复两条相同网关策略导致网关报错的问题；</strong></li><li>【组件库管理】<strong>修复应用模版release状态展示错误的问题；</strong></li><li>【资源统计】<strong>修复团队使用资源统计中磁盘使用量统计错误的问题；</strong></li><li>【应用管理】<strong>修复应用治理模式切换错误提示的问题；</strong></li><li>【应用管理】<strong>修复恢复时删除原应用下组件导致恢复失败的问题；</strong></li><li>【应用管理】<strong>修复升级时未变更组件仍然进行了滚动更新的问题；</strong></li><li>【应用管理】<strong>修复升级时只发布部分组件，导致升级后依赖丢失的问题；</strong></li><li>【组件管理】<strong>修复组件配置文件名称校验错误的问题；</strong></li><li>【组件管理】<strong>修复第三方组件实例数与初始化状态错误的问题；</strong></li></ul><br>
<br><img src="https://static.goodrain.com/dingdingqun.jpeg" alt="请输入图片名称" referrerpolicy="no-referrer">
                                
                                                              
</div>
            