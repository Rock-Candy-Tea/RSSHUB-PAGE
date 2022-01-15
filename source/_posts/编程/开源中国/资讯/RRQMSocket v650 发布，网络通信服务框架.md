
---
title: 'RRQMSocket v6.5.0 发布，网络通信服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3901'
author: 开源中国
comments: false
date: Sat, 15 Jan 2022 16:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3901'
---

<div>   
<div class="content">
                                                                                            <p>RRQMSocket v6.5.0 已经发布，网络通信服务框架。</p> 
<p>此版本更新内容包括：</p> 
<div> 
 <pre><code>版本号:6.5
更新日期：2022.1.15
更新描述：本次更新TCP适配器更新较大，但都能很快修改。

【RRQMCore】
修复：ByteBlock.ReadFloat()返回值错误bug。
增加：ByteBlock.ToArray(int position,int length)，可以直接导出实际真实内存。

【RRQMSocket】
修改：DataHandlingAdapter类，回调参数由ByteBlock+object改为ByteBlock+IRequestInfo。
修改：FixedHeaderDataHandlingAdapter类，改名为FixedHeaderPackageAdapter。
修改：FixedSizeDataHandlingAdapter类，改名为FixedSizePackageAdapter。
修改：TerminatorDataHandlingAdapter类，改名为TerminatorPackageAdapter。
修改：DataAdapterTester类，修改相关参数及启动方法，详情请看单元测试。
修改：TCP系类，修改处理函数为HandleReceivedData(ByteBlock byteBlock, IRequestInfo requestInfo)。
修改：Simple服务器类，修改类名为对应服务器泛型类型。
增加：DataAdapterTester类，增加性能时间评估，详情请看单元测试。
增加：CustomDataHandlingAdapter类，该类能更大程度的简化用户处理数据的逻辑。
增加：CustomFixedHeaderDataHandlingAdapter类，该类基本能解决所有固定包头类似协议的数据。
增加：CustomUnfixedHeaderDataHandlingAdapter类，该类基本能解决所有非固定包头类似协议的数据（如HTTP）。
增加：Channel类，增加HoldOn指令，调用该指令时，接收方会跳出接收，但是通道依然可用。
</code></pre> 
</div> 
<p>详情查看：<a href="https://gitee.com/dotnetchina/RRQMSocket/releases/v6.5.0">https://gitee.com/dotnetchina/RRQMSocket/releases/v6.5.0</a></p>
                                        </div>
                                      
</div>
            