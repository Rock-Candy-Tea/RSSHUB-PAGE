
---
title: '类 Electron 开发框架 HorseJs 0.0.11 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e9fc1c8a94ce1ad596d02e3fa99c64301cb.png'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 02:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e9fc1c8a94ce1ad596d02e3fa99c64301cb.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div>
  <span style="color:#0451a5">-</span>
  <span style="color:#000000"> 打开新窗口后迅速关闭窗口会导致应用崩溃的问题</span>
 </div> 
 <div>
  <span style="color:#0451a5">-</span>
  <span style="color:#000000"> DEMO 示例创建托盘图标，图标位置不正确的问题</span>
 </div> 
 <div>
  <span style="color:#0451a5">-</span>
  <span style="color:#000000"> 没创建托盘图标的情况下，直接修改托盘图标的路径会导致应用异常</span>
 </div> 
 <div>
  <span style="color:#0451a5">-</span>
  <span style="color:#000000"> 对返回的错误信息进行 utf-8 编码</span>
 </div> 
 <div>
  <span style="color:#0451a5">-</span>
  <span style="color:#000000"> 更新 TS 类型，使其支持 strict 模式</span>
 </div> 
 <div>
  <span style="color:#0451a5">-</span>
  <span style="color:#000000"> 右键菜单支持分割线，支持选中菜单项，支持禁用菜单项</span>
 </div> 
 <div>
   
 </div> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="786" src="https://oscimg.oschina.net/oscnet/up-e9fc1c8a94ce1ad596d02e3fa99c64301cb.png" width="600" referrerpolicy="no-referrer"></p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt height="786" src="https://oscimg.oschina.net/oscnet/up-642ba462e0cdde94edf147f8fb5a08555f3.png" width="600" referrerpolicy="no-referrer"></p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">HorseJs 是一个与 Electron 类似的框架，与 Electron 不同的是它没有内置 Node.js，而是直接使用 C++ 提供了大部分 Electron 的能力，比如使用 JavaScript 访问文件、打开对话框、创建新窗口等。由于没有 Node.js，所以 HorseJs 运行速度更快、占用内存更少、稳定性也更高。</p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">HorseJs 可以直接加载 webpack 或 Rollup 构建的任何前端项目，由于这些构建工具会把 npm 包内的代码捆扎到你的最终产物中，所以开发者可以在这类项目中使用任何 npm 包，HorseJs 并不排斥 Node.js 的生态。</p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">使用 HorseJs 开发应用，不必考虑任何渲染进程、主进程以及这些进程之间通信的问题。因为这些工作 HorseJs 已经帮开发者做掉了。开发者只要专注自己的业务逻辑即可。</p> 
</div>
                                        </div>
                                      
</div>
            