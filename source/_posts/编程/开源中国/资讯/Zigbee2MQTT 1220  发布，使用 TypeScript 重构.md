
---
title: 'Zigbee2MQTT 1.22.0  发布，使用 TypeScript 重构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1103/072648_1asl_5430600.png'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 23:28:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1103/072648_1asl_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Zigbee2MQTT 1.22.0 版本已发布，<span style="color:#333333">Zigbee2MQTT是一个将 Zigbee 协议转化成 MQTT 的桥接工具，允许通过 MQTT 协议控制 Zigbee 设备。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本主要更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">TypeScript <span style="color:#333333">重构</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>TypeScript 重构已经完成，现在 Zigbee2MQTT 完全用 TypeScript 编写。这个重构给外部扩展带来了一些变化：<span> </span><code>onMQTTConnected()</code><span> </span>和<span> </span><code>onZigbeeStarted()</code><span> </span>被替换<code>start()</code>，<code>onMQTTMessage()</code><span> </span>和<span> </span><code>onZigbeeEvent()</code>方法不再自动调用，需通过订阅<span> </span><code>eventbus</code><span> </span>。</li> 
 <li>此版本还推出了由<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpsi-4ward" target="_blank">psi-4ward</a><span> </span>创建的新站点。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">特性</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F6281" target="_blank">#6281</a><span style="color:#24292f"> </span>可用性功能已重新实现，添加了更多功能，提高了可靠性并减轻网络压力。旧配置仍然有效 (<span> </span><code>advanced.availability_timeout</code>) ，不过建议更新<span> </span><code>configuration.yaml</code><span> </span>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fpull%2F9056" target="_blank">#9056</a><span> </span><span style="color:#2e3033">现在允许在前端创建和回调场景。</span></li> 
</ul> 
<p><img alt height="276" src="https://static.oschina.net/uploads/space/2021/1103/072648_1asl_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fpull%2F9110" target="_blank">#9110</a><span> </span><span style="color:#2e3033">现在允许在前端管理设备选项。</span></li> 
</ul> 
<p><img alt height="349" src="https://static.oschina.net/uploads/space/2021/1103/072726_prgt_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#2e3033">改进</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3109" target="_blank">#3109</a> <span style="color:#24292f">为 Develco EMIZB-132 添加 OTA 支持。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3112" target="_blank">#3112</a> <span style="color:#24292f">支持 ubisys D1 / D1-R 的 minimum_on_level。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3121" target="_blank">#3121</a><span> </span>更新 neo.js ：公开<span> </span><span style="color:#24292f">NAS-PD07</span><span> </span>的<span> </span><span style="color:#24292f"><code>battery_low</code></span>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F8956" target="_blank">#8956</a><span> </span>初始 MQTT 连接失败时，停止 Zigbee2MQTT 并报错。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3119" target="_blank">#3119</a><span> </span>为 Develco EMIZB-132 和 SMSZB-120 添加固件版本报告。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3083" target="_blank">#3083</a><span> </span>为 easyCodeTouch_v1 添加 pin 码编程、呈现动作和自动重新锁定。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F8287" target="_blank">#8287</a><span> </span>家庭助理：启用时查找 last_seen 传感器。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fissues%2F3068" target="_blank">#3068</a><span> </span>提高<span> </span><span style="color:#24292f">TuYa</span><span> </span>设备访问的稳定性。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnurikk%2Fzigbee2mqtt-frontend%2Fissues%2F926" target="_blank">#926</a><span> </span>允许通过端点 ID 寻找设备。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3158" target="_blank">#3158</a><span> </span>改善小米 SJCGQ11LM 的曝光温度。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3164" target="_blank">#3164</a><span> </span>改进对 Busch-Jaeger 6735/6736/6737 的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3166" target="_blank">#3166</a><span> </span>小米 QBKG39LM、QBKG38LM、QBKG25LM 现在支持 mode_switch 。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fpull%2F9214" target="_blank">#9214</a><span> </span><span style="color:#2e3033">向 Home Assistant 公开设备和组 configuration_url 。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F9147" target="_blank">#9147</a><span> </span>Woox R7049 现在支持烟雾测试。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fpull%2F9312" target="_blank">#9312</a><span> </span>为<span> </span><span style="color:#24292f">Home Assistant</span><span> </span>实体添加计量单位</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3227" target="_blank">#3227</a><span> </span>为 YSR-MINI-Z 添加操作模式</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3222" target="_blank">#3222</a><span> </span> 为 IKEA E1525/E1745 曝光<span> </span><code>illuminance_above_threshold</code><span> </span>，添加<code>illuminance_below_threshold_check</code>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3241" target="_blank">#3241</a><span> </span>为<span> </span><span style="color:#24292f">OSRAM 4062172044776 </span><span> </span>公开 2 个端点。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fissues%2F3066" target="_blank">#3066</a><span> </span>修复 EMIZB-132 能量除数的错误。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F7423" target="_blank">#7423</a><span> </span>修复某些设备主题的 last_seen 属性未更的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3107" target="_blank">#3107</a><span> </span>修复 TuYa TS011F （制造商名称：<code>_TZ3000_dpo1ysak</code>）的功率监控问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F8959" target="_blank">#8959</a><span> </span>修复外部转换器不加载的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3145" target="_blank">#3145</a><span> </span>修复某些<span> </span><span style="color:#24292f">Yale lock<span> </span></span>电池百分比不正确的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F8769" target="_blank">#8769<span> </span></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F8617" target="_blank">#8617</a><span> </span>修复<span> </span><span style="color:#24292f">Home Assistant<span> </span></span>模板变量警告问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F9085" target="_blank">#9085</a><span> </span>修复 Node.js 10 兼容性。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F9133" target="_blank">#9133</a><span> </span>修复转换器抛出异常时的崩溃。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3171" target="_blank">#3171</a><span> </span>修复<span> </span><code>window_open_internal</code><span> </span>的命名错误。<span style="color:#24292f">(closing -> closed)</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3176" target="_blank">#3176</a><span> </span>修复<span> </span><span style="color:#24292f">Danfoss 和 Popp 恒温器</span>的<span> </span><code>setpoint_change_source</code>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fissues%2F3122" target="_blank">#3122</a><span> </span>修复<span> </span><span style="color:#24292f">Assistant fix discovery</span><span> </span>仅支持倾斜覆盖的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fissues%2F3086" target="_blank">#3086</a><span> </span>修复 Sunricher SR-ZG9001K12-DIM-Z4 的 2、3 、4 按钮不起作用的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3203" target="_blank">#3202</a><span> </span>修复 3RWS18BZ 的电源问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3201" target="_blank">#3201</a><span> </span>修复 Eurotronic 恒温器的<span> </span><code>running_state</code><span style="color:#24292f"><span> </span>值总是<span> </span><code>null<span> </span></code>的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fpull%2F9268" target="_blank">#9268</a><span> </span>修复<span> </span><span style="color:#24292f">Assistant fix discovery<span> </span></span>选择将数字作为选项的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fpull%2F3218" target="_blank">#3218</a><span> </span>修复 TRADFRI LED1624G9 不支持色温的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F9057" target="_blank">#9057</a><span> </span>修复 TS011F _TZ3000_cphmq0q7 的功率测量问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee-herdsman-converters%2Fissues%2F3229" target="_blank">#3229<span> </span></a>修复<span> </span><span style="color:#24292f">Home Assistant number 为 0 时，最大/最小值不正确的问题。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Fissues%2F8349" target="_blank">#8349</a><span> </span>修复 GL-SD-001 的亮度命令超时问题。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">除以上内容，此版本还添加了对 75 款新设备的支持，详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FKoenkk%2Fzigbee2mqtt%2Freleases" target="_blank">点击查看更新公告</a>。</p>
                                        </div>
                                      
</div>
            