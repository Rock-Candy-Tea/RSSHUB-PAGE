
---
title: 'Netflix实用API设计2：Protobuf FieldMask变更操作'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211024/685457877dcf517a05df6ced0f8041a8.jpg'
author: Dockone
comments: false
date: 2021-10-27 14:08:07
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211024/685457877dcf517a05df6ced0f8041a8.jpg'
---

<div>   
<br><h3>背景</h3>在我们<a href="http://dockone.io/article/2434655">之前的文章</a>中，我们讨论了在设计API时如何利用<a href="https://developers.google.com/protocol-buffers/docs/reference/csharp/class/google/protobuf/well-known-types/field-mask">FieldMask</a>作为解决方案，以便消费者可以按需通过gRPC获取请求的数据。在这篇博文中，我们将继续介绍Netflix Studio Engineering如何使用FieldMask进行更新和删除等变更操作。<br>
<h3>案例：Netflix Studio Production</h3>之前我们概述了什么是Production以及Production服务如何对其他微服务进行gRPC调用，例如Schedule服务和Script服务，它们是用于检索特定产品（例如 La Casa De Papel）的schedule和script。我们可以采用该模型并展示我们如何改变产品中的特定字段。<br>
<h3>修改产品详细信息</h3>假设我们作品添加了一些动画元素，想要将format字段从LIVE_ACTION更新为HYBRID。一个比较笨的方法是添加一个updateProductionFormatRequest方法，然后gRPC服务端来更新productionFormat：<br>
<pre class="prettyprint">message UpdateProductionFormatRequest &#123;<br>
string id = 1;<br>
ProductionFormat format = 2;<br>
&#125;<br>
<br>
service ProductionService &#123;<br>
rpc UpdateProductionFormat (UpdateProductionFormatRequest) <br>
  returns (UpdateProductionFormatResponse);<br>
&#125; <br>
</pre><br>
这的确可以让我们更新特定产品格式（format），但是如果我们想要更新其他字段（例如标题）或多个字段（例如 productionFormat、schedule 等），该怎么办？按照这个处理方法，我们应该为每个字段实现一个更新方法：一个用于产品格式，另一个用于标题等等：<br>
<pre class="prettyprint">// separate RPC for every field, not recommended<br>
service ProductionService &#123;<br>
rpc UpdateProductionFormat (UpdateProductionFormatRequest) &#123;...&#125;<br>
<br>
rpc UpdateProductionTitle (UpdateProductionTitleRequest) &#123;...&#125;<br>
<br>
rpc UpdateProductionSchedule (UpdateProductionScheduleRequest) &#123;...&#125;<br>
<br>
rpc UpdateProductionScripts (UpdateProductionScriptsRequest) &#123;...&#125;<br>
&#125;<br>
<br>
message UpdateProductionFormatRequest &#123;...&#125;<br>
<br>
message UpdateProductionTitleRequest &#123;...&#125;<br>
<br>
message UpdateProductionScheduleRequest &#123;...&#125;<br>
<br>
message UpdateProductionScriptsRequest &#123;...&#125; <br>
</pre><br>
当产品中的字段数量很多时，对API的维护将会变得很难。如果我们想要更新多个字段并在单个RPC中以原子方式进行怎么办？为各种字段组合创建额外的方法将会导致API的爆炸式增长。此解决方案不可扩展。<br>
<br>与其尝试创建每个可能的组合，另一种解决方案是服务端提供UpdateProduction接口，该接口需要消费者提供所有字段：<br>
<pre class="prettyprint">message Production &#123;<br>
string id = 1;<br>
string title = 2;<br>
ProductionFormat format = 3;<br>
repeated ProductionScript scripts = 4;<br>
ProductionSchedule schedule = 5;<br>
// ... more fields<br>
&#125;<br>
<br>
service ProductionService &#123;<br>
rpc UpdateProduction (UpdateProductionRequest) returns (UpdateProductionResponse);<br>
&#125;<br>
<br>
message UpdateProductionRequest &#123;<br>
Production production = 1;<br>
&#125; <br>
</pre><br>
此解决方案存在两个问题，首先消费者必须知道并提供Production中的每个必需字段，即使他们只想更新一个字段（例如format）。另一个问题是，由于Production有许多字段，因此请求负载可能会变得非常大，特别是Production有schedule或scripts信息。<br>
<br>如果我们只发送我们实际想要更新的字段而不是所有字段，同时让所有其他字段处于未设置状态，该怎么办？在我们的示例中，我们将只设置产品实例的format字段（和用于引用产品实例的ID ）：<br>
<pre class="prettyprint">UpdateProduction updateProduction = UpdateProduction.newBuilder()<br>
.setProductionFormat(PRODUCTION_FORMAT_HYBRID)<br>
.build();<br>
<br>
// Send the update request<br>
UpdateProductionResponse response = client.updateProduction(LA_CASA_DE_PAPEL_PRODUCTION_ID, <br>
updateProductionRequest);<br>
</pre><br>
如果我们永远不需要删除或清空任何字段，那么这种方案倒是没有问题。 但是如果我们想删除title字段的值呢？同样，我们可以引入像RemoveProductionTitle这样的方法，但如上所述，这个解决方案不能很好地扩展。如果我们想从schedule中删除嵌套字段的值，例如计划启动日期字段，该怎么办？我们最终会为每个单独的可以为空的子字段添加相应的删除 RPC。<br>
<h3>利用FieldMask做变更</h3>我们可以利用FieldMask用于变更操作，而不是使用大量RPC或需要大的请求负载。FieldMask将列出我们想要明确更新的所有字段。首先，让我们更新我们的proto文件以添加到UpdateProductionRequest中，它将包含我们想要从一个产品实例中更新的数据，以及应该更新的FieldMask：<br>
<pre class="prettyprint">message ProductionUpdateOperation &#123;<br>
string production_id = 1;<br>
string title = 2;<br>
ProductionFormat format = 3;<br>
ProductionSchedule schedule = 4;<br>
repeated ProductionScript scripts = 5;<br>
... // more fields<br>
&#125;<br>
<br>
message UpdateProductionRequest &#123;<br>
// contains production ID and fields to be updated<br>
ProductionUpdateOperation update = 1;<br>
google.protobuf.FieldMask update_mask = 2;<br>
&#125; <br>
</pre><br>
现在，我们可以使用FieldMask来进行变更操作。我们可以通过使用<a href="https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/util/FieldMaskUtil.html#fromStringList-java.lang.Class-java.lang.">FieldMaskUtil.fromStringList()</a>方法为format字段创建一个FieldMask来更新格式，该方法为特定类型的字段路径列表构造一个FieldMask。在这种情况下，我们将有一种类型，但稍后将基于此示例进行构建：<br>
<pre class="prettyprint">FieldMask updateFieldMask = FieldMaskUtil.fromStringList(Production.class, <br>
Collections.singletonList(“format”);<br>
<br>
// Update the production format type<br>
ProductionUpdateOperation productionUpdateOperation = ProductionUpdateOperation<br>
.newBuilder()<br>
.setProductionId(LA_CASA_DE_PAPEL_PRODUCTION_ID)<br>
.setProductionFormat(PRODUCTION_FORMAT_HYBRID)<br>
.build();<br>
<br>
// Build the UpdateProductionRequest including the updatefieldmask<br>
UpdateProductionRequest updateProductionRequest = UpdateProductionRequest<br>
.newBuilder()<br>
.setUpdate(productionUpdateOperation)<br>
.setUpdateMask(updateFieldMask)<br>
.build();<br>
<br>
// Send the update request<br>
UpdateProductionResponse response = <br>
client.updateProduction(LA_CASA_DE_PAPEL_PRODUCTION_ID, updateProductionRequest);<br>
</pre><br>
由于我们的FieldMask仅指定format字段，即使我们在ProductionUpdateOperation中提供更多数据，该字段也将是唯一更新的字段。通过修改路径，可以更轻松地向我们的FieldMask添加或删除更多字段。 所有未添加到FieldMask路径中的数据将不会被更新并且在操作中会被忽略。另外，如果我们省略一个值同时FieldMask存在该字段，那么将会对该字段执行删除操作。让我们修改上面的示例来演示这一点：更新格式，同时删除计划启动日期，这是ProductionSchedule上的嵌套字段“schedule.planned_launch_date”：<br>
<pre class="prettyprint">FieldMask updateFieldMask = FieldMaskUtil.fromStringList(Production.class,<br>
Arrays.asList("format", "schedule.planned_launch_date"));<br>
<br>
// Update the format, in addition remove schedule.planned_launch_date by not including it in our request<br>
ProductionUpdateOperation productionUpdateOperation = ProductionUpdateOperation<br>
.newBuilder()<br>
.setProductionId(LA_CASA_DE_PAPEL_PRODUCTION_ID)<br>
.setProductionFormat(PRODUCTION_FORMAT_HYBRID)   <br>
.build();<br>
<br>
UpdateProductionRequest updateProductionRequest = UpdateProductionRequest<br>
.newBuilder()<br>
.setUpdate(productionUpdateOperation)<br>
.setUpdateMask(updateFieldMask)<br>
.build();<br>
<br>
// Send the update request<br>
UpdateProductionResponse response = <br>
client.updateProduction(LA_CASA_DE_PAPEL_PRODUCTION_ID, updateProductionRequest);<br>
</pre><br>
在这个例子中，我们向FieldMask添加了“format”和“schedule.planned_launch_date”路径，那么就会执行更新和删除操作。当我们在负载数据中提供这些字段时，这些字段将更新为新值，但在构建负载数据时，如果我们仅提供format并省略schedule.planned_launch_date，那么 这将表示我们要对该省略的字段执行删除操作：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211024/685457877dcf517a05df6ced0f8041a8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211024/685457877dcf517a05df6ced0f8041a8.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>空/缺失Field Mask</h3>当FieldMask未设置或没有路径时，更新操作将作用于所有负载字段。这意味着调用者必须发送整个负载字段，或者如上所述，任何未设置的字段都将被删除。<br>
<br>这个约定对模式演化有影响：当一个新字段被添加到消息中时，所有消费者必须在更新操作中发送它的值，否则它将被删除。<br>
<br>假设我们要添加一个新字段：产品预算。我们需要扩展Production消息和ProductionUpdateOperation：<br>
<pre class="prettyprint">// update operation with new ‘budget’ field<br>
message ProductionUpdateOperation &#123;<br>
string production_id = 1;<br>
string title = 2;<br>
ProductionFormat format = 3;<br>
ProductionSchedule schedule = 4;<br>
repeated ProductionScript scripts = 5;<br>
ProductionBudget budget = 6;            // new field<br>
&#125; <br>
</pre><br>
如果有一个消费者不知道这个新字段或者还没有更新客户端存根（stubs），它可能会意外地通过在更新请求中不发送这个FieldMask将预算字段清空。<br>
<br>为了避免这个问题，生产者可以考虑要求所有更新操作都设置该字段掩码。另一种选择是实现版本控制协议：强制所有调用者发送他们的版本号并实现自定义逻辑来跳过旧版本中不存在的字段。<br>
<h3>总结</h3>在本博文系列中，我们讨论了在Netflix如何使用FieldMask，以及在设计API时如何使它成为实用且可扩展的解决方案。<br>
<br>API设计者应该以简单为目标，同时具有很好的扩展和演化性。保持API简单且面向未来通常并不容易。在API中使用FieldMask有助于我们实现简单性和灵活性。<br>
<br><strong>原文链接：<a href="https://netflixtechblog.com/practical-api-design-at-netflix-part-2-protobuf-fieldmask-for-mutation-operations-2e75e1d230e4">Practical API Design at Netflix, Part 2: Protobuf FieldMask for Mutation Operations</a>（翻译：王欢）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            