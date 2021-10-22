
---
title: 'api-result 2.5.0 发布，API 接口返回结果规范化解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7653'
author: 开源中国
comments: false
date: Fri, 22 Oct 2021 10:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7653'
---

<div>   
<div class="content">
                                                                    
                                                        <p>api-result 2.5.0 已经发布，API 接口返回结果规范化解决方案。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li>【变更】ResultTemplate，code 类型改为 Integer</li> 
 <li>【变更】ResultTemplate，msg 改为 message</li> 
 <li>【变更】IReturnCode，getErrCode() 改为 getCode()</li> 
 <li>【变更】IReturnCode，getMsg() 改为 getMessage()</li> 
 <li>【变更】IReturnCode，getErrCode() 返回类型改为 Integer</li> 
 <li>【变更】IReturnCode，成功的返回码改为 0</li> 
 <li>【变更】IReturnCode，错误的返回码改为 -1</li> 
 <li>【变更】IReturnCode，Default，枚举错误去掉前缀 ERROR</li> 
 <li>【变更】ResultTemplate 更名为 ResponseTemplate</li> 
 <li>【变更】ResultHeader 更名为 ResponseHeader</li> 
 <li>【删除】ResultTemplate，删除 errCode</li> 
 <li>【删除】ResultTemplate，删除 errMsg</li> 
 <li>【删除】IReturnCode，删除 ERROR_SYSTEM_EXCEPTION</li> 
 <li>【删除】ResultHeader，删除默认的 traceId 属性</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/fengwenyi/api-result/releases/2.5.0">https://gitee.com/fengwenyi/api-result/releases/2.5.0</a></p>
                                        </div>
                                      
</div>
            