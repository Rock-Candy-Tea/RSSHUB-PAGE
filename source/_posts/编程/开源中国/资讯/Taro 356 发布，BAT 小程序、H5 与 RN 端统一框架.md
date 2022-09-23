
---
title: 'Taro 3.5.6 发布，BAT 小程序、H5 与 RN 端统一框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1805'
author: 开源中国
comments: false
date: Fri, 23 Sep 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1805'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Taro 3.5.6 现已发布。Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 等应用。具体更新内容如下：</span></p> 
<h4>特性</h4> 
<p><strong>小程序</strong></p> 
<ul> 
 <li>支持使用 Vue3 编译原生自定义组件</li> 
</ul> 
<p><strong>RN</strong></p> 
<ul> 
 <li>默认使用 react-native <code>0.69</code> 版本，并增加了对 React18 的支持</li> 
</ul> 
<p><strong>Typings</strong></p> 
<ul> 
 <li>重构类型系统，根据各小程序官方文档，补全小程序组件类型声明文件（相关讨论：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2F11740" target="_blank">#11740</a>）</li> 
</ul> 
<h4>修复</h4> 
<p><strong>小程序</strong></p> 
<ul> 
 <li>修复微信小程序对 <code>showShareMenu</code> API 的支持</li> 
 <li>修复微信小程序对 <code>cropImage</code> API 的支持，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12524" target="_blank">#12524</a></li> 
 <li>修复 <code>webpack-sources</code> 版本不一致带来的问题</li> 
 <li>修复 Webpack5 预编译导致 Vue3 报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12340" target="_blank">#12340</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12090" target="_blank">#12090</a></li> 
 <li>修复 Webpack5 预编译导致京东小程序、百度小程序报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12414" target="_blank">#12414</a></li> 
 <li>修复 Webpack5 预编译导致 Vue devtools 报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12452" target="_blank">#12452</a></li> 
 <li>修复支付宝小程序使用 <code>CustomWrapper</code> 失败的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12496" target="_blank">#12496</a></li> 
 <li>优化组件收集逻辑。修复使用 Vue 渲染函数、或使用第三方组件库时，报找不到对应 template 模板的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F9740" target="_blank">#9740</a></li> 
 <li>按需生成 <code>CustomWrapper</code> 产物，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F11745" target="_blank">#11745</a></li> 
</ul> 
<p><strong>H5</strong></p> 
<ul> 
 <li>修复 <code>Input</code> 组件在 <code>type=number maxlength=-1</code> 的情况下内容无法输入问题</li> 
 <li>组件库导出 SourceMap</li> 
 <li>修复 <code>Input</code> 组件 <code>type</code> 属性为 <code>number</code> 或 <code>digit</code> 时,输入特殊符号导致交互异常的问题</li> 
 <li>修复页面 <code>onShow</code> 时 <code>onReachBottom</code> 事件多次触发的问题</li> 
 <li>支持捕获 <code>Video</code> 组件 <code>hls</code> 流中的错误信息</li> 
 <li>修复 <code>pxtransform</code> API 转换尺寸错误的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12475" target="_blank">#12475</a></li> 
 <li>修复 Webpack5 预编译导致构建报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12385" target="_blank">#12385</a></li> 
 <li>修复开启多页应用模式报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12417" target="_blank">#12417</a></li> 
 <li>修复自定义环境变量导致的 mode 错误，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12436" target="_blank">#12436</a></li> 
</ul> 
<p><strong>RN</strong></p> 
<ul> 
 <li>修复引入同名 style 文件时变量名冲突的问题</li> 
 <li>升级 CLI 默认安装的 <code>expo</code> 版本到 <code>~46.0.1</code></li> 
 <li>修复 <code>showActionSheet</code> API 在 RN Android 端与其他端不一致的问题</li> 
 <li>修复 <code>Input</code> 和 <code>TextArea</code> 组件在 <code>focus</code> 属性变更时聚焦失焦不同步的问题</li> 
</ul> 
<p><strong>PostCSS</strong></p> 
<ul> 
 <li>修复 <code>postcss.pxtransform.config.baseFontSize</code> 参数无效的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12449" target="_blank">#12449</a></li> 
 <li>修复 <code>autoprefixer</code> warning</li> 
</ul> 
<p><strong>CLI</strong></p> 
<ul> 
 <li>修复 <code>taro convert</code> 命令报错的问题，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12309" target="_blank">#12309</a></li> 
</ul> 
<h4>Typings</h4> 
<ul> 
 <li>修复定位 API 的类型定义</li> 
 <li>更新 <code>createOffscreenCanvas</code> API 的类型定义，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fissues%2F12391" target="_blank">#12391</a></li> 
 <li>修复 <code>openBusinessView</code> API 的类型定义</li> 
</ul> 
<h4>Breaking changes</h4> 
<p><strong>RN</strong></p> 
<p>版本升级仔细阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2F12133" target="_blank">https://github.com/NervJS/taro/discussions/12133</a></p> 
<ul> 
 <li>0.69 版本最低支持 iOS 12.4</li> 
 <li>expo-av 在 0.68 需要锁定版本</li> 
 <li>如使用 Playground 调试，react-native-gesture-handler 版本需要对应</li> 
 <li>初始化 0.68 版本的 RN：<code>taro init --template-source github:NervJS/taro-project-templates#v3.5-RN-0.68</code></li> 
</ul> 
<p><span style="color:#333333">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Freleases%2Ftag%2Fv3.5.6" target="_blank">https://github.com/NervJS/taro/releases/tag/v3.5.6</a></p>
                                        </div>
                                      
</div>
            