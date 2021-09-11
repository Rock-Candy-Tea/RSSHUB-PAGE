
---
title: 'Midway 2.13.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7746'
author: 开源中国
comments: false
date: Sat, 11 Sep 2021 15:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7746'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div class="lake-content" typography="classic"> 
  <h2 id="QHEnF" style="font-size: 24px; line-height: 32px; margin: 21px 0 5px 0"><span class="ne-text">Features</span></h2> 
  <h3 id="tvodr" style="font-size: 20; line-height: 28px; margin: 16px 0 5px 0"><span class="ne-text">1、添加一批新组件</span></h3> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="u0c813a5e"><span class="ne-text">多进程下只在单一进程执行逻辑的组件 </span><code class="ne-code" style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace; background-color: rgba(0, 0, 0, 0.06); border: 1px solid rgba(0, 0, 0, 0.08); border-radius: 2px; padding: 0px 2px"><span class="ne-text">@midwayjs/process-agent</span></code><span class="ne-text"> （测试）</span></li> 
   <li id="uce9a1805"><span class="ne-text">sequelize 组件 </span><code class="ne-code" style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace; background-color: rgba(0, 0, 0, 0.06); border: 1px solid rgba(0, 0, 0, 0.08); border-radius: 2px; padding: 0px 2px"><span class="ne-text">@midwayjs/sequelize</span></code><span class="ne-text"> （测试）</span></li> 
  </ul> 
  <h3 id="ScLwN" style="font-size: 20; line-height: 28px; margin: 16px 0 5px 0"><span class="ne-text">2、增加了一批 DTO 方法</span></h3> 
  <p class="ne-p" id="uf3b46d57" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">感谢社区 @</span><a class="ne-link" data-href="https://github.com/fuguohong" href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffuguohong" target="_blank"><span class="ne-text">fuguohong</span></a><span class="ne-text"> 提供此 PR。</span></p> 
  <p class="ne-p" id="u1f96e2ea" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">具体内容如下：</span></p> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="ub55ab3cb"><span class="ne-text">增加</span><code class="ne-code" style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace; background-color: rgba(0, 0, 0, 0.06); border: 1px solid rgba(0, 0, 0, 0.08); border-radius: 2px; padding: 0px 2px"><span class="ne-text">function PickDto<T, K extends keyof T>(dto: Dto<T>,keys: K[]): Dto<Pick<T, typeof keys[number]>></span></code><span class="ne-text"> 用于生成新的只包含指定字段的dto</span></li> 
   <li id="ub87efc2a"><span class="ne-text">增加 </span><code class="ne-code" style="font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace; background-color: rgba(0, 0, 0, 0.06); border: 1px solid rgba(0, 0, 0, 0.08); border-radius: 2px; padding: 0px 2px"><span class="ne-text">function OmitDto<T, K extends keyof T>(dto: Dto<T>,keys: K[]):Dto<Omit<T,typeof keys[number]>></span></code><span class="ne-text"> 用于生成新的不包含指定字段的dto</span></li> 
  </ul> 
  <ul class="ne-ul" style="margin: 0; padding-left: 23px"> 
   <li id="u0111aa10"><span class="ne-text">dto 支持继承，可以不用再写 class 的 Rule 装饰器了</span></li> 
   <li id="uec01d3aa"><span class="ne-text">RuleOptions 增加 min 和 max 字段用于支持 dto 数组字段的最大最小长度限制</span></li> 
  </ul> 
  <h2 id="ftRMq" style="font-size: 24px; line-height: 32px; margin: 21px 0 5px 0"><span class="ne-text">Bugfix</span></h2> 
  <h3 id="IOJGe" style="font-size: 20; line-height: 28px; margin: 16px 0 5px 0"><span class="ne-text">1、透出在 Serverless 事件触发器下的报错</span></h3> 
  <p class="ne-p" id="u489788ab" style="margin: 0; padding: 0; min-height: 24px"><span class="ne-text">之前版本在事件触发器下遗漏了报错信息的输出，新版本修复了该问题。</span></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            