
---
title: 'Serverless Devs 2.1.2 发布，Serverless 开发者平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5536'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 17:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5536'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Serverless Devs 2.1.2 已经发布，Serverless 开发者平台。</p> 
<p>此版本更新内容包括：</p> 
<h3>FEATURE</h3> 
<ul> 
 <li>在 CD 环境下，不检测 cli 更新逻辑</li> 
 <li>s.yaml 支持模板引擎</li> 
 <li>publish yaml 新增一个 x-departed 字段</li> 
 <li>s config add 样式修改</li> 
 <li>执行 action 模块 在 window 中默认使用 CMD 的 shell 报错时进行提示</li> 
 <li>setupEnv()兼容边缘 case</li> 
 <li>s clean --all 遇到文件权限不够的时候，进行 Error 提示</li> 
</ul> 
<h3>BUGFIX</h3> 
<ul> 
 <li>无法在子目录中校验根目录下有继承关系的 s.yaml 文件的合规性</li> 
 <li>Exec Command Removed But Local Invoke Guide To Use it</li> 
 <li>req.body 的内容与预期不一致</li> 
 <li>s invoke <local/start> for python3.9 runtime causing invalid ELF header error</li> 
 <li>EDIT 功能在选择的时候有点问题，例如 NASConfig，选择自动配置貌似出现的是自定义配置？</li> 
 <li>s init 对于定时触发器 payload （jsonstring）里的魔法变量 替换不正确。</li> 
 <li>s init 不支持带中文字符的 s.yaml</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/serverless-devs/Serverless-Devs/releases/2.1.2">https://gitee.com/serverless-devs/Serverless-Devs/releases/2.1.2</a></p>
                                        </div>
                                      
</div>
            