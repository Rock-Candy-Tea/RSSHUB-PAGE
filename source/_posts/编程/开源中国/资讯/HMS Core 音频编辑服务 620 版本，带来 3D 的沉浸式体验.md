
---
title: 'HMS Core 音频编辑服务 6.2.0 版本，带来 3D 的沉浸式体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2909ed1c2449ede90c957c6ac4c989133d1.png'
author: 开源中国
comments: false
date: Wed, 15 Dec 2021 08:50:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2909ed1c2449ede90c957c6ac4c989133d1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>在音乐创作、音视频剪辑和游戏等领域中，给用户带来沉浸式音频体验越来越重要。开发者如何在应用内打造3D环绕声效？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fhms%2Fhuawei-audio-editor%2F%3Fha_source%3Dhms1" target="_blank">华为音频编辑服务</a>6.2.0版本此次带来了空间动态渲染功能，可以将人声、乐器等音频元素渲染到指定的三维空间方位，支持静态和动态渲染两种模式，进一步提升应用中的音效体验。开发者可以点击查看以下Demo演示，了解集成效果并上手实验功能特性。</p> 
<h2>开发实战</h2> 
<h3>1. 开发准备</h3> 
<p>开发者提前准备音乐素材，MP3格式最佳。其他音频格式请参考“2.4”步骤转换，视频格式请参考“2.5”步骤进行音频提取。</p> 
<p><strong>1.1项目级build.gradle里配置Maven仓地址</strong>：</p> 
<pre><code>buildscript &#123;
    repositories &#123;
        google()
        jcenter()
        // 配置HMS Core SDK的Maven仓地址。
        maven &#123;url 'https://developer.huawei.com/repo/'&#125;
    &#125;
    dependencies &#123;
        ...
        // 增加agcp插件配置。
        classpath 'com.huawei.agconnect:agcp:1.4.2.300'
    &#125;
&#125;
allprojects &#123;
    repositories &#123;
        google()
        jcenter()
        // 配置HMS Core SDK的Maven仓地址。
        maven &#123;url 'https://developer.huawei.com/repo/'&#125;
    &#125;
&#125; 
</code></pre> 
<p><strong>1.2 文件头增加配置</strong>：</p> 
<pre><code>apply plugin: 'com.huawei.agconnect'
</code></pre> 
<p><strong>1.3 应用级build.gradle里配置SDK依赖</strong>：</p> 
<pre><code>dependencies&#123;
    implementation 'com.huawei.hms:audio-editor-ui:&#123;version&#125;'
&#125;
</code></pre> 
<p><strong>1.4在AndroidManifest.xml文件中申请如下权限</strong>：</p> 
<pre><code><!--震动权限-->
<uses-permission android:name="android.permission.VIBRATE" />
<!--麦克风权限-->
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<!--写存储权限-->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<!--读存储权限-->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<!--网络权限-->
<uses-permission android:name="android.permission.INTERNET" />
<!--网络状态权限-->
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<!--网络状态变化权限-->
<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
</code></pre> 
<h3>2.代码开发</h3> 
<p><strong>2.1创建应用自定义的activity界面，用于选择音频，并将该音频文件路径返回给音频编辑SDK</strong>：</p> 
<pre><code>// 将音频文件路径List返回到音频编辑页面
private void sendAudioToSdk() &#123;
    // 获取到的音频文件路径 filePath
    String filePath = "/sdcard/AudioEdit/audio/music.aac";
    ArrayList<String> audioList = new ArrayList<>();
    audioList.add(filePath);
    // 将音频文件路径返回到音频编辑页面
    Intent intent = new Intent();
    // 使用sdk提供的HAEConstant.AUDIO_PATH_LIST
    intent.putExtra(HAEConstant.AUDIO_PATH_LIST, audioList);
    // 使用sdk提供的HAEConstant.RESULT_CODE为结果CODE
    this.setResult(HAEConstant.RESULT_CODE, intent);
    finish();
&#125;
</code></pre> 
<p><strong>2.2在UI界面导入音频时，SDK会发送一个action值为com.huawei.hms.audioeditor.chooseaudio的intent以跳转到该activity。因此，该activity“AndroidManifest.xml”中的注册形式如下</strong>：</p> 
<pre><code><activity android:name="Activity "> 
<intent-filter> 
<action android:name="com.huawei.hms.audioeditor.chooseaudio"/> 
<category android:name="android.intent.category.DEFAULT"/> 
</intent-filter> 
</activity>
</code></pre> 
<p><strong>2.3启动音频编辑页面，点击“添加音频”，SDK会主动调用“2.1”步骤中定义的activity。添加好音频，就可以进行音频编辑、特效添加等操作，完成后导出编辑音频</strong>。</p> 
<pre><code>HAEUIManager.getInstance().launchEditorActivity(this);
</code></pre> 
<p><strong>2.4.如果音频素材不是MP3格式，此步骤可以完成音频格式转换</strong>：</p> 
<p>调用transformAudioUseDefaultPath接口进行音频格式转换，转换后的音频文件导出到默认路径。</p> 
<pre><code>// 音频格式转换接口
HAEAudioExpansion.getInstance().transformAudioUseDefaultPath(context,inAudioPath, audioFormat, new OnTransformCallBack() &#123;
    // 进度回调（0-100）
    @Override
    public void onProgress(int progress) &#123;
    &#125;
    // 转换失败
    @Override
    public void onFail(int errorCode) &#123;
    &#125;
    // 转换成功
    @Override
    public void onSuccess(String outPutPath) &#123;
    &#125;
    // 取消转换
    @Override
    public void onCancel() &#123;
    &#125;
    &#125;);

// 取消转换任务接口
HAEAudioExpansion.getInstance().cancelTransformAudio();
</code></pre> 
<p>调用transformAudio接口进行音频格式转换，转换后的音频文件导出到目标路径。</p> 
<pre><code>// 音频格式转换接口
HAEAudioExpansion.getInstance().transformAudio(context,inAudioPath, outAudioPath, new OnTransformCallBack()&#123;
    // 进度回调（0-100）
    @Override
    public void onProgress(int progress) &#123;
    &#125;
    // 转换失败
    @Override
    public void onFail(int errorCode) &#123;
    &#125;
    // 转换成功
    @Override
    public void onSuccess(String outPutPath) &#123;
    &#125;
    // 取消转换
    @Override
    public void onCancel() &#123;
    &#125;
    &#125;);
// 取消转换任务接口
HAEAudioExpansion.getInstance().cancelTransformAudio();
</code></pre> 
<p><strong>2.5如果素材是视频格式，可以调用extractAudio接口进行音频提取，从视频中提取音频文件再导出到指定目录</strong>：</p> 
<pre><code>// outAudioDir提取出的音频保存的文件夹路径，非必填
// outAudioName提取出的音频名称，不带后缀，非必填
HAEAudioExpansion.getInstance().extractAudio(context,inVideoPath,outAudioDir, outAudioName,new AudioExtractCallBack() &#123;
    @Override
    public void onSuccess(String audioPath) &#123;
    Log.d(TAG, "ExtractAudio onSuccess : " + audioPath);
    &#125;
    @Override
    public void onProgress(int progress) &#123;
    Log.d(TAG, "ExtractAudio onProgress : " + progress);
    &#125;
    @Override
    public void onFail(int errCode) &#123;
    Log.i(TAG, "ExtractAudio onFail : " + errCode);
    &#125;
    @Override
    public void onCancel() &#123;
    Log.d(TAG, "ExtractAudio onCancel.");
    &#125;
    &#125;);
// 取消音频提取任务接口
HAEAudioExpansion.getInstance().cancelExtractAudio();
</code></pre> 
<p><strong>2.6调用getInstruments和startSeparationTasks接口进行伴奏提取</strong>。</p> 
<pre><code>// 获取提取伴奏类型ID，后面将此ID传给接口
HAEAudioSeparationFile haeAudioSeparationFile = new HAEAudioSeparationFile();
haeAudioSeparationFile.getInstruments(new SeparationCloudCallBack<List<SeparationBean>>() &#123;
    @Override
public void onFinish(List<SeparationBean> response) &#123;
// 返回的数据，包括伴奏的类型ID
&#125;
    @Override
    public void onError(int errorCode) &#123;
        // 失败返回
&#125;
&#125;);
// 设置要提取的伴奏参数
List instruments = new ArrayList<>();
instruments.add(“伴奏id”);
haeAudioSeparationFile.setInstruments(instruments);
// 开始进行伴奏分离
haeAudioSeparationFile.startSeparationTasks(inAudioPath, outAudioDir, outAudioName, new AudioSeparationCallBack() &#123;
    @Override
    public void onResult(SeparationBean separationBean) &#123; &#125;
    @Override
    public void onFinish(List<SeparationBean> separationBeans) &#123;&#125;
    @Override
    public void onFail(int errorCode) &#123;&#125;
    @Override
    public void onCancel() &#123;&#125;
&#125;);
// 取消分离任务
haeAudioSeparationFile.cancel();
</code></pre> 
<p><strong>2.7调用applyAudioFile接口进行空间方位渲染</strong>。</p> 
<pre><code>// 空间方位渲染
// 固定摆位
HAESpaceRenderFile haeSpaceRenderFile = new HAESpaceRenderFile(SpaceRenderMode.POSITION);
haeSpaceRenderFile.setSpacePositionParams(
                            new SpaceRenderPositionParams(x, y, z));
// 动态渲染
HAESpaceRenderFile haeSpaceRenderFile = new HAESpaceRenderFile(SpaceRenderMode.ROTATION);
haeSpaceRenderFile.setRotationParams( new SpaceRenderRotationParams(
                                    x, y, z, surroundTime, surroundDirection));
// 扩展
HAESpaceRenderFile haeSpaceRenderFile = new HAESpaceRenderFile(SpaceRenderMode.EXTENSION);
haeSpaceRenderFile.setExtensionParams(new SpaceRenderExtensionParams(radiusVal, angledVal));
// 调用接口
haeSpaceRenderFile.applyAudioFile(inAudioPath, outAudioDir, outAudioName, callBack);
// 取消空间方位渲染
haeSpaceRenderFile.cancel();
</code></pre> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2909ed1c2449ede90c957c6ac4c989133d1.png" referrerpolicy="no-referrer"></p> 
<p>完成以上步骤，就可以得到对应的空间动态渲染效果，在应用内轻松实现2D转3D音效啦！这项功能还可以应用到企业会议以及运动康复领域，比如在展会上进行产品沉浸式展示、作为视障人群的方向感线索，为日常生活提供便利等。开发者们可以根据自己应用的实际需求选择使用，如需了解更多详情，请参考： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fhms%2Fhuawei-audio-editor%2F%3Fha_source%3Dhms1" target="_blank">华为开发者联盟音频编辑服务官网</a>; 获取<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fdoc%2Fdevelopment%2FMedia-Guides%2Fclient-dev-0000001107465102%3Fha_source%3Dhms1" target="_blank">集成音频编辑服务指导文档</a>。</p> 
<p><strong>了解更多详情>></strong></p> 
<p>访问<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fhms%3Fha_source%3Dhms1" target="_blank">华为开发者联盟官网</a><br> 获取<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdeveloper.huawei.com%2Fconsumer%2Fcn%2Fdoc%2Fdevelopment%3Fha_source%3Dhms1" target="_blank">开发指导文档</a><br> 华为移动服务开源仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgithub.com%2FHMS-Core" target="_blank">GitHub</a>、<a href="http://gitee.com/hms-core">Gitee</a></p> 
<p><strong>关注我们，第一时间了解 HMS Core 最新技术资讯~</strong></p>
                                        </div>
                                      
</div>
            