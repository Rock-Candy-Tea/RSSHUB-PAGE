
---
title: 'smart-license v1.0.4 发布，为软件提供授权的工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5400'
author: 开源中国
comments: false
date: Fri, 21 May 2021 15:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5400'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">smart-license 是一款用于安全加固的开源项目。 主要服务于非开源产品、商业软件、具备试用功能的付费软件等，为软件提供授权制的使用方式。</p> 
<p style="text-align:start"><strong>名词解释：</strong></p> 
<ul> 
 <li>License：通过 smart-license 生成的授权文件，导入至要授权使用的软件产品中。</li> 
 <li>源数据：需要进行 License 加工处理的基础数据。例如，将软件产品运行的配置文件作为<strong>源数据</strong>，经由 smart-license 授权处理后生成 License 文件。</li> 
 <li>License源文件：生成 License 的同时，会自动产生一份文件用于记录：源数据，授权时间，过期时间，秘钥对等信息。由软件授权方持有，当客户遗失 License 文件之后可以根据<strong>License源文件</strong>重新生成 License。</li> 
</ul> 
<p style="text-align:start"><strong>适用场景</strong>：</p> 
<ul> 
 <li>非开源产品、商业软件、收费软件。</li> 
 <li>限制产品的传播性，每个客户拥有专属 License。</li> 
 <li>同一款软件发行包根据 License 的不同提供不同的服务能力。</li> 
 <li>限定软件授权时效</li> 
</ul> 
<p style="text-align:start"><strong>产品特色：</strong></p> 
<ul> 
 <li>开源，代码完全公开，License的生成原理是透明的。</li> 
 <li>易用，提供二进制包，直接基于命令行生成 License。</li> 
 <li>安全，生成的 License 在一定程度上具备防篡改能力，破解难度大。</li> 
 <li><a href="https://gitee.com/smartboot/smart-license/blob/master/security.md">安全加固</a>，采用非对称加密方式对 License源数据进行预处理，防止伪造License。</li> 
</ul>
                                        </div>
                                      
</div>
            