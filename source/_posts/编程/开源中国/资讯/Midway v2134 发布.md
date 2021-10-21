
---
title: 'Midway v2.13.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=751'
author: 开源中国
comments: false
date: Thu, 21 Oct 2021 15:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=751'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span>双十一大促期间，我们的发版周期会变长，请谅解。</span> </p> 
<div> 
 <div> 
  <div> 
   <div> 
    <div> 
     <h2 style="margin-left:0; margin-right:0"><span>Features</span></h2> 
     <h3 style="margin-left:0; margin-right:0"><span>1、新增 mongoose 组件</span></h3> 
     <ul style="margin-left:0; margin-right:0"> 
      <li><span>1、mongoose 组件可以独立使用，typegoose 组件基于 mongoose 组件，用户原有使用不变</span></li> 
      <li><span>2、得益于 mongoose 组件的升级，typegoose 也同步支持了多 mongoose 实例（灰度）</span> </li> 
      <li><span>3、升级支持的 mongoose 版本到 v6，升级支持的 typegoose 版本到 v9</span></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0"><strong><span>Bugfix</span></strong></h2> 
     <h3 style="margin-left:0; margin-right:0"><span>1、修复加载组件使用对象形式的问题</span></h3> 
     <p style="margin-left:0; margin-right:0"><span>旧版在加载组件时，如果使用对象形式且没有配置 enabledEnvironment 时，会自动忽略组件加载。新版本修复了该问题。</span></p> 
     <pre>@Configuration(&#123;
imports: [
    &#123;
    target: xxxx// 旧版本这样写会忽略这个组件加载
    &#125;
  ]
&#125;)
</pre> 
     <h3 style="margin-left:0; margin-right:0"><span>2、static-layer 在处理 prefix 时更加友好</span></h3> 
     <p style="margin-left:0; margin-right:0"><span>之前用户在 yml 中必须配置 prefix 时增加 </span><code><span>/</span></code><span> 。新版本做了优化，会自动增加。</span></p> 
     <pre>service: my-static-demo

provider:
  name: aliyun                

deployType: 
  type: static
  config:
    prefix: api                ## 这里没有前缀会自动增加

package:                      
  include: build </pre> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            