
---
title: 'sitesCMS v3.1.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=208'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 19:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=208'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0; text-align:justify"> 
  <h3 style="margin-left:0; margin-right:0">sitesCMS简介</h3> 
  <p style="color:inherit; margin-left:0; margin-right:0">sitesCMS 是基于 JFinal 的 多站点 CMS内容管理系统，遵循JFinal极简设计理念，轻量级、易扩展、学习简单，除JFinal外无其他重度依赖。精简的多站点功能设计，极易二次开发，一天一个网站不是梦。完善的API模块，支持 微信小程序 、APP等各类小程序前端对接，打通移动端开发渠道，sitesCMS 不只是 CMS。<br> 官方网站：<code>http://sitescms.top/</code><br> 视频教程：<code>https://ke.qq.com/course/3551225?tuin=92419b8c</code></p> 
  <h3 style="margin-left:0; margin-right:0">更新内容</h3> 
  <p style="color:inherit; margin-left:0; margin-right:0">【升级】升级log4j版本至1.2.17<br> 【优化】优化表单token校验功能，提取通用拦截器，简化Controller中的代码</p> 
  <h3 style="margin-left:0; margin-right:0">扩展知识</h3> 
  <p style="color:inherit; margin-left:0; margin-right:0">介绍一个JFinal的扩展知识，在拦截器中获取返回内容，并对内容进行更新，这也是本次更新的主要代码，通过这次的更新进行演示说明。</p> 
  <pre style="margin-left:0; margin-right:0"><code>public <span style="color:inherit"><span style="color:#f82375">class</span> <span style="color:#a5da2d">ReturnInterceptor</span> <span style="color:#f82375">implements</span> <span style="color:#a5da2d">Interceptor</span> </span>&#123;

    <span style="color:#5bdaed">@Override</span>
    public <span style="color:#f82375">void</span> intercept(Invocation invocation) &#123;
        invocation.invoke();<span style="color:#808080">//先执行后续的逻辑</span>

        Controller controller = invocation.getController();
        Render render = controller.getRender();<span style="color:#808080">//获取返回的render</span>
        <span style="color:#f82375">if</span>(render instanceof JsonRender)&#123;<span style="color:#808080">//判断render类型</span>
            JsonRender jsonRender = (JsonRender) render;
            <span style="color:#f82375">String</span> jsonText = jsonRender.getJsonText();<span style="color:#808080">//获取返回字符串内容</span>
            JSONObject jsonObject = JSONUtil.parseObj(jsonText);
            <span style="color:#f82375">String</span> state = (<span style="color:#f82375">String</span>) jsonObject.<span style="color:#f82375">get</span>(<span style="color:#eedc70">"state"</span>);
            <span style="color:#f82375">if</span>(<span style="color:#eedc70">"fail"</span>.equals(state))&#123;
                <span style="color:#808080">//失败的情况下重新生成token并返回</span>
                jsonObject.<span style="color:#f82375">set</span>(SiteInfo.formTokenKey, controller.createToken(SiteInfo.formTokenKey, <span style="color:#ae87fa">1800</span>));
                <span style="color:#808080">//将更新后的内容返回</span>
                controller.renderJson(jsonObject);
            &#125;
        &#125;
    &#125;

&#125;</code></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            