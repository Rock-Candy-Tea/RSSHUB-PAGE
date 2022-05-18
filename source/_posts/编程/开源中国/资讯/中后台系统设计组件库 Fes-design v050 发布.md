
---
title: '中后台系统设计组件库 Fes-design v0.50 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8811'
author: 开源中国
comments: false
date: Wed, 18 May 2022 14:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8811'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Fes-design“快速、简单、稳定”的中后台系统设计组件库”</p> 
<h1><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcompare%2Fv0.4.7...v0.5.0" target="_blank">0.5.0</a> (2022-05-13)</h1> 
<h3>Breaks</h3> 
<ul> 
 <li>重构Cascader组件，改为使用SelectCascader组件 * 去掉VirtualList组件的 rootTag 属性</li> 
</ul> 
<h3>Bug Fixes</h3> 
<ul> 
 <li>当popper弹窗大小改变时,需要更新位置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F138" target="_blank">#138</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F42affea7e6fe30e872d0021302c5251fc201d7f8" target="_blank">42affea</a>)</li> 
 <li>Date-picker range 选择，输入框宽度优化 + datetime 支持hourStep minuteStep secondStep + timepicker 交互优化 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F140" target="_blank">#140</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2Fa973b43ab74547edd2fa83c35be00ef06316e6bf" target="_blank">a973b43</a>)</li> 
 <li>dragable 动态插入值，不能拖拽问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F146" target="_blank">#146</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2Fa3c9f89fc974e344d7155d278f831d63627f4689" target="_blank">a3c9f89</a>)</li> 
 <li>Form组件的inline模式下row-gap在78存在兼容性问题,改为grid实现 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F141" target="_blank">#141</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F3c9ac12ac9b62d5384482d926cc351203f00f012" target="_blank">3c9ac12</a>)</li> 
 <li>input-number 修复 form 校验不通过时，边框变红问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F148" target="_blank">#148</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2Fa3b602c1cfdc1b4c77e5905914eb02bc3be6042c" target="_blank">a3b602c</a>)</li> 
 <li>scrollbar能监听内容大小更新 & 去掉z-index (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F151" target="_blank">#151</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F3f676cb7cce7a17ae4c613ee349a0c62f3dac7bc" target="_blank">3f676cb</a>)</li> 
 <li>Select当只有option只有value时,可自定义内容展示，默认展示 value (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F149" target="_blank">#149</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2Fd7879c134ad842508c2cee29369e6d87904aeff4" target="_blank">d7879c1</a>)</li> 
 <li>Table组件修复因为fixed导致表头和列不一致的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F150" target="_blank">#150</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F9935f2db12cf3052e1981c1263b9c5263fe153c5" target="_blank">9935f2d</a>)</li> 
 <li>upload的close按钮居中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F139" target="_blank">#139</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F9754f635dc2eea12c041e832de976815dd461f68" target="_blank">9754f63</a>)</li> 
</ul> 
<h3>Features</h3> 
<ul> 
 <li>Date picker range 支持输入 + 自定义 format (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F147" target="_blank">#147</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2Fe737fb05c9d2b7383877ba322b9b1ec28dbf3866" target="_blank">e737fb0</a>)</li> 
 <li>input[text] 支持 showWordLimit (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F145" target="_blank">#145</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F9249db87eabe18e5f76595f519cdc633bf3596e9" target="_blank">9249db8</a>)</li> 
 <li>tabs 添加 change 事件 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fissues%2F142" target="_blank">#142</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FWeBankFinTech%2Ffes-design%2Fcommit%2F003ec6e2888fb120864b3d1a630cba465f7c8fdb" target="_blank">003ec6e</a>)</li> 
 <li>Scrollbar增加contentStyle、horizontalRatioStyle、verticalRatioStyle配置</li> 
</ul>
                                        </div>
                                      
</div>
            