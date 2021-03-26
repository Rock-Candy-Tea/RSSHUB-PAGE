
---
title: 'EVM 3.0 发布，迈向超轻量物联网浏览器更进一步'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2f7d647c1c96246f0b084f1fc91f549411e.png'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 09:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2f7d647c1c96246f0b084f1fc91f549411e.png'
---

<div>   
<div class="content">
                                                                                            <h1>1. EVM是什么？</h1> 
<p><strong><code>EVM</code></strong><span style="color:#333333"> 全称 </span><code>Embedded Virtual Machine</code><span style="color:#333333">，本质上是一款通用、精简的嵌入式虚拟机，由语法解析前端框架和字节码运行后端构成，可运行在资源受限制的单片机上。</span></p> 
<p><img alt height="883" src="https://oscimg.oschina.net/oscnet/up-2f7d647c1c96246f0b084f1fc91f549411e.png" width="746" referrerpolicy="no-referrer"></p> 
<h1>2. EVM物联网应用生态建设</h1> 
<p><img alt height="1105" src="https://oscimg.oschina.net/oscnet/up-9e60a2fd543da200ea1c822d6a189043179.png" width="746" referrerpolicy="no-referrer"></p> 
<h1>3. 更新内容</h1> 
<ul> 
 <li>增加cortex-m3/m4/a9平台支持;</li> 
 <li>增加bouffalolab博流BL602芯片支持;</li> 
 <li>增加cat1 4G芯片ASR3601芯片支持;</li> 
 <li>增加IOT.js支持，为物联网提供一个基于 Web 技术的可相互操作的服务平台;</li> 
 <li>增加对MicroPython的兼容支持，原生支持js调用micropython的标准库和第三方库;</li> 
 <li>增加对WebAssembly的原生支持，可以将C/C++/Java/Go/Rust等语言编译成WASM，在JS层原生调用wasm的API;</li> 
 <li>ecma增加unicode支持</li> 
 <li>EVUE增加lvgl5.3的支持，原生兼容lvgl5.3/lvgl7;</li> 
 <li>EVUE模拟器增加对lvgl5.3支持，支持在线运行evue和epk应用</li> 
 <li>发布《EVM 应用开发标准 1.0》</li> 
 <li>更新在线帮助手册；</li> 
 <li>更新项目目录结构，支持集成更多RTOS和组件、模块；</li> 
</ul> 
<h1>4.快速体验</h1> 
<ul> 
 <li>启动器和启动器内每个应用直接从云端获取应用包，实时渲染；</li> 
</ul> 
<div> 
 <div> 
  <div> 
   <pre><span style="color:#595959"><span style="color:#595959"><span style="color:#6f42c1">cd</span> tools/evuesimulator-20210326090615-8e30a0e
</span></span><span style="color:#595959"><span style="color:#595959">./evue.exe C:/test/watch_launcher</span></span>
</pre> 
  </div> 
 </div> 
</div> 
<div>
 <img alt height="382" src="https://oscimg.oschina.net/oscnet/up-2a88d2a6da01dec02acaf44321bfe9b27af.gif" width="746" referrerpolicy="no-referrer">
</div> 
<p> </p> 
<ul> 
 <li>关于模拟器的更多介绍和使用，请参考：<span style="color:#abb2bf"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fbytecode%2Fevue%2Fvdtprt" target="_blank">https://www.yuque.com/bytecode/evue/vdtprt</a></span></li> 
 <li>真机体验视频链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1G54y1h7XK%2F" target="_blank">https://www.bilibili.com/video/BV1G54y1h7XK/</a></li> 
</ul> 
<h1>5. 效果展示</h1> 
<ul> 
 <li>js原生调用WebAssembly的wasm文件</li> 
</ul> 
<p><img alt height="453" src="https://oscimg.oschina.net/oscnet/up-bc99f9916a7ee2fab6095bb9bfa07f351ab.png" width="746" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>js原生调用micropython的第三方库</li> 
</ul> 
<p><img alt height="439" src="https://oscimg.oschina.net/oscnet/up-356cd7e593c9d7c576b88535c5ea8cc9ec6.png" width="604" referrerpolicy="no-referrer"></p> 
<p><img alt height="409" src="https://oscimg.oschina.net/oscnet/up-0a8a5b8f392f76872696665291a6e34ac4a.png" width="470" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>EVUE 启动器</li> 
</ul> 
<p><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-c0a8a9820467d93549a6cd3b2c21fe3b8be.png" width="240" referrerpolicy="no-referrer"><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-c091c9fd189d0ee29c1839a539266a001fe.png" width="240" referrerpolicy="no-referrer"><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-ce8fc110144dcb94dd9c170e9703b6b3724.png" width="240" referrerpolicy="no-referrer"><img alt height="240" src="https://oscimg.oschina.net/oscnet/up-3da217c12210c6d535f87f4894a9ad5748d.png" width="240" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>EVM应用商店</li> 
</ul> 
<p><img alt height="364" src="https://oscimg.oschina.net/oscnet/up-d30b26fbb2c8998167958cddca53d9ceb05.png" width="746" referrerpolicy="no-referrer"></p> 
<h1>6. 下个版本更新计划</h1> 
<ul> 
 <li>继续完善IOT.js支持；</li> 
 <li>继续完善micropython支持；</li> 
 <li>重构增强evm超轻量物联网浏览器引擎；</li> 
 <li>继续完善对cat1芯片的适配支持；</li> 
 <li>增加对ESP32开发板支持；</li> 
 <li>增加华为云组件支持；</li> 
</ul> 
<h1>7. EVM在线帮助手册</h1> 
<ul> 
 <li><a href="http://scriptiot.gitee.io/evm_doc/#/zh-cn/evm_what" target="_blank">EVM在线帮助手册Gitee</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fscriptiot.github.io%2Fevm_doc%2F%23%2Fzh-cn%2Fevm_what" target="_blank">EVM在线帮助手册Github</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fbooks%2Fshare%2F07c6dc3d-5343-45dd-a7d2-fd5ccaa05825%3F%23+%E3%80%8AEVM+%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E6%A0%87%E5%87%86%E3%80%8B" target="_blank">《EVM应用开发标准1.0》</a></li> 
</ul> 
<h1>8. EVM 芯片支持计划</h1> 
<p>EVM团队愿意携手广大的芯片厂家和方案公司，给物联网行业的开发者推出更加简单高效的解决方案，打破物联网和互联网人才边界，赋能物联网企业和开发者提供全新的开发模式，降低物联网开发门槛，极速提升开发效率。</p> 
<div> 
 <table border="1" cellspacing="0" style="width:737px"> 
  <tbody> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px; text-align:center; vertical-align:middle; white-space:normal"> <p>芯片</p> </td> 
    <td style="border-color:#d9d9d9; height:33px; text-align:center; white-space:normal"> <p>应用场景</p> </td> 
    <td rowspan="1" style="background-color:#ffffff; border-color:#d9d9d9; height:33px; text-align:center; vertical-align:top; white-space:normal"> <p>方案</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px; text-align:center; white-space:normal"> <p>ASR3601</p> </td> 
    <td style="border-color:#d9d9d9; height:33px; text-align:center; white-space:normal"> <p><span style="color:#505050">可用于功能机、儿童手表、POS机、对讲机、智能音箱等应用</span></p> </td> 
    <td rowspan="1" style="background-color:#ffffff; border-color:#d9d9d9; height:33px; text-align:center; vertical-align:top; white-space:normal"> <p>基于EVM的物联网小程序解决方案</p> <p>基于EVM的应用商店解决方案</p> </td> 
   </tr> 
   <tr> 
    <td style="border-color:#d9d9d9; height:33px; text-align:center; white-space:normal"> <p>stm32L4R9</p> </td> 
    <td style="border-color:#d9d9d9; height:33px; text-align:center; white-space:normal"> <p><span style="color:#000000">健康手环,智能手表,小型医疗设备,智能表计和智能工业传感器</span></p> </td> 
    <td rowspan="1" style="background-color:#ffffff; border-color:#d9d9d9; height:33px; text-align:center; vertical-align:middle; white-space:normal"> <p>基于EVM的物联网小程序解决方案</p> </td> 
   </tr> 
   <tr> 
    <td colspan="1" style="background-color:#ffffff; border-color:#d9d9d9; text-align:center; vertical-align:top; white-space:normal"> <p>BL602</p> </td> 
    <td colspan="1" style="background-color:#ffffff; border-color:#d9d9d9; text-align:center; vertical-align:top; white-space:normal"> <p>Wi-Fi + BLE 组合(大写)的芯片组,用于低功耗和高性能应用开发</p> </td> 
    <td colspan="1" style="background-color:#ffffff; border-color:#d9d9d9; text-align:center; vertical-align:middle; white-space:normal"> <p>基于EVM的服务应用解决方案</p> </td> 
   </tr> 
  </tbody> 
 </table> 
</div> 
<h1>9. 项目地址</h1> 
<ul> 
 <li>Gitee: <a href="https://gitee.com/scriptiot/evm" target="_blank">https://gitee.com/scriptiot/evm</a></li> 
 <li>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscriptiot%2Fevm" target="_blank">https://github.com/scriptiot/evm</a></li> 
</ul>
                                        </div>
                                      
</div>
            