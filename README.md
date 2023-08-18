# webshell_pcap_decode

基于 ctf 面向 realworld 的 webshell 流量包分析解密工具

> 支持 pcap、pcapng 等格式

一键展示命令与返回结果的配对

<img width="384" alt="image" src="https://github.com/cns1rius/webshell_pcap_decode/assets/73370907/033c4370-20e7-45af-84fd-4fb2fd37a44b">

目前正在第一阶段完成三大 webshell 管理工具的 php 马部分

后续将添加 jsp 部分（咕咕咕）

asp、csharp 也有可能（可能性不大）

> 部分源码改自 @webraybtl/[webshell_detect](https://github.com/webraybtl/webshell_detect)

## 使用方法

`python main.py xxx.pcap(ng)`

结果保存在./data.txt(覆盖式写入、需要保存时记得另存）

## 更新日志

- 8、16 更新 已完成 Godzila_PHP_Eval_Xor_Base64_decode 部分（Behinder 目前还不能用）
