
---
title: '新增商品弹框组件的实现（Demo）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5df52f4996734fc08581e7434c09bf62~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 18:00:44 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5df52f4996734fc08581e7434c09bf62~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">技术栈：</h2>
<p>umi + antd + ts</p>
<h2 data-id="heading-1">先看效果:</h2>
<h3 data-id="heading-2">1.点击+符号，弹出新增商品组件</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5df52f4996734fc08581e7434c09bf62~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.新增商品弹框内容</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbb1ba1eef1d4d24ad54f3de7b9f4ffb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">文件目录</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7b76f471dff43f7ab0b819d1edb0717~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">文件解析</h2>
<h5 data-id="heading-6">const.ts</h5>
<pre><code class="copyable">export const formLayout = &#123;
  labelCol: &#123; // 标签大小
    sm: &#123; span: 6 &#125;,
    xs: &#123; span: 24 &#125;
  &#125;,
  wrapperCol: &#123; // 输入控件的大小
    sm: &#123; span: 16 &#125;,
    xs: &#123; span: 24 &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec1736d32c624d30bc7c42219ac718f9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d86a0cce3254da8af2552bbcbc908c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8451d1a0687b4d3ca0905980c861664c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">index.tsx</h5>
<p>实现效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/613a8aa3216a4c15902bc8809163cfb9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">import React, &#123; useState &#125; from 'react'
import &#123; Tooltip &#125; from 'antd'
import &#123; PlusCircleOutlined &#125; from '@ant-design/icons'

import './index.styl' // 引入样式
import AddShopModal from './addShop' // 引入新增商品组件

export default () => &#123;
  const [state, setState] = useState(&#123; // 控制商品组件是否 可见 或者 可编辑
    isEditAddShop: false,
    addShopVisible: false
  &#125;)

  /**
 - 打开/关闭新增商品组件弹窗
 - @param visible
 - @param isEdit
 - ?：可选参数--可有可无
   */
  const handleToggleAddShop = (visible: boolean, isEdit?: boolean) => &#123;
    // ...state 设置初始状态，如果有参数传入，值发送变化，则 isEditAddShop: isEdit, addShopVisible: visible 覆盖state的值
    setState(&#123; ...state, isEditAddShop: isEdit, addShopVisible: visible &#125;)
  &#125;

  return (
    <> // 最外层 div 可以省略
      <div>
        <Tooltip title='新增商品'>
          <PlusCircleOutlined onClick=&#123;() => handleToggleAddShop(true, false)&#125; />
        </Tooltip>
      </div>
      <AddShopModal
        isEdit=&#123;state.isEditAddShop&#125; // 新增商品 是否可编辑 通过 prop 传递 state.isEditAddShop的值给 新增商品组件，从而控制是否编辑状态 
        visible=&#123;state.addShopVisible&#125; // 同理上面
        onClose=&#123;() => handleToggleAddShop(false)&#125;
      />
    </>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">addShop.tsx</h5>
<p>分步骤解析</p>
<ul>
<li>文件导入</li>
</ul>
<p>// 新建商品组件</p>
<p>import React, &#123; useState, useEffect &#125; from 'react' </p>
<p>import &#123; Button, Modal, Form, Input, Select, Upload, message &#125; from 'antd' </p>
<p>import &#123; PlusCircleOutlined, DeleteOutlined, DownloadOutlined, UploadOutlined &#125; from '@ant-design/icons' </p>
<p>import _ from 'lodash' </p>
<p>import &#123; generate &#125; from 'shortid' </p>
<p>import &#123; Store &#125; from 'antd/lib/form/interface' </p>
<p>import &#123; formLayout &#125; from './const' // 用来定义label标签和输入控件的大小与间隔 </p>
<p>import &#123; ShopComponent &#125; from '@/interfaces/shop-component' </p>
<p>import &#123; uploadAddShopFile &#125; from '@/services/shop-component/addShop' // 新增商品接口 </p>
<p>import &#123; useCommit, useLoading, useModelState &#125; from '@/models/shop-component/addShop-model' // 调用接口/数据存储的实现方法</p>
<h3 data-id="heading-9">规范注意点：</h3>
<p>1.从外部导入的文件/插件等，统一放在最上面，一起放 </p>
<p>2.从内部导入的文件/插件等，统一放在外部导入的文件/插件 的 下面 （可以隔开一格来区分）</p>
<p>这里引用了shortid 里面的 generate，用于生成唯一的 key，这样我们点击 添加参数 时，就可以不断新增不重复的项（key不同），因为React中，每一项都需要一个 唯一的key 去区分不同的项</p>
<p>formLayout 放在这里使用</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/862f2d512b17457eaa6e396b738ec65f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>ShopComponent 为 Interface接口 定义 数据类型命名和契约</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00df0fb6724041688461aff3cb739afa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">export declare namespace ShopComponent &#123;
  // 商品类型参数
  interface SParamsType &#123;
    key?: string,
    name: string,
    anName: string,
    value: string,
    type: string
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 declare声明 了 namespace命名空间</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbb0f80768044d5dbc7a5f36f8d3911c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>定义好从父组件传递过来的数据的类型</p>
<p>interface InitProps &#123;
isEdit: boolean
visible: boolean
onClose: () => void
&#125;</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b533f20bf574e8aa1fd42470f974050~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>void</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa43cf99e3e44014a52e58c3a282e54f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f76c917b9c84f21b41746ffd1a58fe9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>文本域和选择器选项</li>
</ul>
<p>const &#123; TextArea &#125; = Input // 引用 文本域 组件 </p>
<p>const &#123; Option &#125; = Select // 引用 选择器的 选项</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ad332e83d254a9f99b015bb9830c2af~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88bd6be465204973a92057f0d7947391~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">商品弹框组件编写</h2>
<h2 data-id="heading-11">第一步：初始化数据，定义state</h2>
<pre><code class="copyable">export default function AddShopModal(props: InitProps) &#123; // props 接受父组件传过来的数据
  
  const initParams: ShopComponent.SParamsType = &#123; // 定义类型 并 初始化 ShopComponent 商品类型参数
    key: generate(), // 随机生成唯一的id,作为key
    name: '',
    anName: '',
    value: '',
    type: 'input'
  &#125;

  const &#123; onClose, visible, isEdit &#125; = props // 对象解构
  const [form] = Form.useForm() // 表单form常用功能，要调用form里面的功能，需要定义下
  const [uploading, setUploading] = useState(false) // 上传按钮loading状态的state
  const [filePath, setFilePath] = useState('') // 设置文件路径state
  const [dataParams, setDataParams] = useState([initParams]) // 设置商品类型-添加参数的state
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c991aeddf5345fabcc3a1960c40f4a0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">第二步：编写组件需要使用到的方法</h2>
<h3 data-id="heading-13">1.关闭当前弹窗并清空列表</h3>
<pre><code class="copyable"> function handleClose() &#123;
    onClose()
    form.resetFields() // 置空form里面的内容
    setFilePath('') // 把文件路径state变为''
    setUploading(false) // 上传状态修改为false
    setDataParams([initParams]) // 商品类型的添加参数变为初始值--initParams
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.商品类型-添加参数-点击添加参数按钮时，先深拷贝(拷贝出来的都是与之前的不相等，不同的栈中，独立的)当前数组，再push（向数组的末尾添加一个或多个元素），这样就形成新的数组</h3>
<pre><code class="copyable">function handleAddParams() &#123;
    const newDataParams = _.cloneDeep(dataParams) // 深拷贝
    newDataParams.push(initParams)
    setDataParams(newDataParams)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">3.删除商品类型-添加参数，先深拷贝当前数组，通过过滤，把当前点击的数组子项过滤掉，这样便形成新的数组，从而删除掉选中项</h3>
<pre><code class="copyable">function handleDeleteParams(key: string) &#123;
    let newDataParams = _.cloneDeep(dataParams)
    newDataParams = _.filter(newDataParams, item => item.key !== key)
    setDataParams(newDataParams)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">4.新增或编辑商品类型-添加参数里面的内容，通过遍历添加参数里面的每一项，拿到当前编辑的项的key与遍历到的key对比，如果相同，则更新为最新的值</h3>
<pre><code class="copyable">  /**
   * 存储商品类型内容变化
   * @param key 每行唯一标识
   * @param field 字段
   * @param value 值
   */
  function handleChangeParams(key: string, field: string, value: string) &#123;
    const newDataParams = _.map(dataParams, data => &#123;
      if(data.key === key) &#123;
        data[field] = value
      &#125;
      return data
    &#125;)
    setDataParams(newDataParams)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">5.上传文件前校验</h3>
<pre><code class="copyable">  /**
   * @param file
   */
  function handleUploadBefore(file: File) &#123;
    const &#123; name &#125; = file // 工资条.zip
    const suffixFile = _.last(_.split(name,'.')) // zip  切割后，变为一个数组，再去最后一项即可
    if(!_.isEqual(suffixFile, 'zip')) &#123; // 比较后缀是否和设定的格式相等，如果不相等，则提示
      message.error('只支持上传 .zip后缀文件')
      return false
    &#125;
    return true
  &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上传的文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ae1f39e03474b3894da3e6f4091b2d2~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">6.文件上传方法</h3>
<pre><code class="copyable">async function handleUpload(options) &#123; // 这里使用了异步方法，不阻塞
    setUploading(true) // 当选择文件好后，开启加载中的状态，即转圈圈
    const &#123; file &#125; = options // 获取文件信息
    const &#123; success, result &#125;: any = await uploadAddShopFile(file) // 上传文件接口--后面的博客再讲解，获取成功和结果信息
    setUploading(false) // 上传成功后，把加载中的状态取消
    const &#123; name &#125; = file // 文件名字
    if(!success) return message.error(`文件上传失败：$&#123;name&#125;`) // 不成功则提示
    const &#123; path &#125; = result // 文件的路径
    form.setFieldsValue(&#123; // 在form表单中设置从后端返回的文件名
      filename: name
    &#125;)
    setFilePath(path) // 设置后端返回的文件路径
    message.success(`文件上传成功：$&#123;name&#125;`) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">7.渲染商品类型-添加参数表单内容</h3>
<pre><code class="copyable">  /**
   * @param dataParams 表单数据
   */
function renderAddParamsForm(dataParams: ShopComponent.SParamsType) &#123;
    const &#123; name, value, key, anName, type &#125; = dataParams
    return (
      <div 
        key=&#123;key&#125;
      >
        <Input 
          placeholder='别名'
          value=&#123;anName&#125;
          onChange=&#123;(e: React.ChangeEvent) => &#123; 
            const val = _.get(e, 'target.value', '') // 获取修改后的值
            handleChangeParams(key, 'anName', val) // 值改变
          &#125;&#125;
        />
        <Input
          placeholder='名称'
          value=&#123;name&#125;
          onChange=&#123;(e: React.ChangeEvent) => &#123;
            const val = _.get(e, 'target.value', '') 
            handleChangeParams(key, 'name',val) 
          &#125;&#125;
        />
        <Input
          placeholder='默认值'
          value=&#123;value&#125;
          onChange=&#123;(e: React.ChangeEvent) => &#123;
            const val = _.get(e, 'target.value', '')
            handleParamsChange(key, 'value', val)
          &#125;&#125;
        />
        <Input 
          placeholder='类型'
          value=&#123;type&#125;
          hidden=&#123;true&#125;
        />
        &#123;
          <DeleteOutlined onClick=&#123;() => handleDeleteParams(key)&#125;></DeleteOutlined>
        &#125;
      </div>
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：渲染的商品类型-添加参数的每一项，都需要一个不同的key</p>
<h3 data-id="heading-20">8.提交方法</h3>
<pre><code class="copyable">  /**
   * 提交
   */
function handleSubmit() &#123;
    if(!filePath) return message.error('请先上传文件！') // 通过商品文件路径判断是否上传商品
    form.validateFields().then((values: Store): void => &#123; // form 表单检验, 通过antd-form存储在Store里面的值  void 无返回值
      if(!!dataParams.length) &#123; // 判断商品类型-添加参数的长度
        const booValue = _.some(dataParams, item => _.values(item).includes('')) // 判断是否有空值，Boolean
        if(booValue) &#123;
          message.error('请添加参数')
          return 
        &#125;
        // 当新建多个参数时，判断参数的名称是否重复
        if(dataParams.length !== 1) &#123;
          const nameArr = _.map(dataParams, item => item.name);
          if(_.uniq(nameArr).length !== nameArr.length) &#123; // 去重后对比，如果名称有重复，则提示错误
            message.error('参数名称不能重复！')
            return
          &#125;
        &#125;
      &#125;
      const reqParams: ShopComponent.IAddShopParams = &#123; // 定义 form 请求的数据类型，已经获取值
        name: values.name,
        alias: values.alias,
        shopPath: values.shopPath,
        shopId: values.shopId,
        description: values.description,
        filename: values.name,
        filePath: filePath,
        params: dataParams
      &#125;
      if (!_.isEmpty(externalDetails)) &#123; // 如果是编辑的时候，则商品的类型不变，通过uuid来控制
        reqParams.uuid = externalDetails.uuid
        delete reqParams.filePath
      &#125;
      commit('addOrUpdateExternal',[reqParams, handleClose]) // 新增或编辑接口
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">页面元素展示：</h2>
<pre><code class="copyable">return (
    <Modal 
    title=&#123;`$&#123;isEdit ? '编辑' : '新建'&#125;商品组件`&#125; // 通过判断 isEdit 的 Boolean 值 来 显示标题
    destroyOnClose // 关闭时销毁 Modal 里的子元素
    width=&#123;600&#125;
    visible=&#123;visible&#125; // 判断是否可见
    onOk=&#123;handleSubmit&#125;
    onCancel=&#123;handleClose&#125;
    confirmLoading=&#123;loading&#125; // 确定按钮 loading 在提交前有个加载中的状态，确保先提交后确定
    >
      <Form form=&#123;form&#125; &#123;...formLayout&#125;> // form 经 Form.useForm() 创建的 form 控制实例，不提供时会自动创建
        <Form.Item
          label='商品组件名称'
          required
          name='alias'
          rules=&#123;[
            &#123; required: true, message: '请输入商品组件名称' &#125;,
            &#123; max: 50, message: '商品组件名称不能超过50个字符' &#125;
          ]&#125;
        >
          <Input placeholder='请输入商品组件名称' />
        </Form.Item>
        <Form.Item 
          label='商品组件标识' 
          required
          name='name'
          rules=&#123;[
            &#123; required: true, message: '请输入商品组件标识' &#125;,
            &#123; max: 50, message: '商品组件标识不能超过50个字符！' &#125;,
            &#123; // 验证规则
              pattern: new RegExp('[^a-zA-Z1-9\-]', 'i'), // 正则表达式
              message: '商品组件标识需由小写英文字母、-、数字组成，不超过50个字符！',
              validator: (rule, value, callback) => &#123;
                if (rule.pattern.test(value)) &#123;
                  callback(rule.message as string)
                &#125;
                callback()
              &#125;
            &#125;
          ]&#125;
        >
          <Input placeholder='请输入商品组件标识' />
        </Form.Item>
        <Form.Item
          label='启动文件路径' 
          required
          name='shopPath'
          rules=&#123;[
            &#123; required: true, message: '请输入启动文件路径' &#125;
          ]&#125;
        >
          <Input placeholder='请输入启动文件路径' />
        </Form.Item>
        <Form.Item 
          label='商品类型'
          required
          name='shopId'
          rules=&#123;[
            &#123; required: true, message: '请选择商品类型' &#125;
          ]&#125;
        >
          <Select 
            placeholder='请选择商品类型'
            allowClear
          >
            &#123;_.map(imageList, item => <Option key=&#123;item.uuid&#125; value=&#123;item.uuid&#125;>&#123;item.alias&#125;</Option>)&#125;
          </Select>
        </Form.Item>
        <div>
          <Button type="ghost" shape="round" icon=&#123;<PlusCircleOutlined />&#125; onClick=&#123;handleAddParams&#125;>
            添加参数
          </Button>
          <div>
            <div>
               <span>别名</span>
               <span>名称</span>
               <span>默认值</span>
            </div>
            &#123;
              _.map(dataParams, item => renderAddParamsForm(item))
            &#125;
          </div>
        </div>
        <Form.Item 
          label='描述'
          required
          name='description'
          rules= &#123;[
            &#123; required: true, message: '请输入描述' &#125;
          ]&#125;
        >
          <TextArea rows=&#123;5&#125; placeholder='请输入描述' />
        </Form.Item>
        <Form.Item
          label='文件名'
          required
          name='filename'
          rules= &#123;[
            &#123; required: true, message: '请输入文件名' &#125;
          ]&#125;
        >
          <Input disabled />
        </Form.Item>
        <div>
          <Upload
            accept='.zip'
            beforeUpload=&#123;file => handleUploadBefore(file)&#125;
            customRequest=&#123;handleUpload&#125;
            showUploadList=&#123;false&#125;
            disabled=&#123;isEdit&#125; // 编辑时禁止上传
          >
            <Button type='primary' icon=&#123;<UploadOutlined/>&#125; loading=&#123;uploading&#125; disabled=&#123;isEdit&#125; >选择上传文件</Button>
          </Upload>
            <Button 
              onClick=&#123;() => window.open("#")&#125; // 这里open本是一个接口，直接可下载示例文件
              type='primary'
              icon=&#123;<DownloadOutlined/>&#125; 
            >
              下载示例文件
            </Button>
        </div>
      </Form>
    </Modal>
)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            