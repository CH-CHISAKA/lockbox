import 'package:flutter/foundation.dart';
import '../models/chat.dart';
import '../models/message.dart';
import '../services/mock_data_service.dart';

class ChatController extends ChangeNotifier {
  List<Chat> _chats = const [];
  final Map<String, List<Message>> _messagesByChat = {};

  List<Chat> get chats => _chats;
  List<Message> messagesFor(String chatId) => _messagesByChat[chatId] ?? const [];

  ChatController() {
    loadChats();
  }

  Future<void> loadChats() async {
    await Future<void>.delayed(const Duration(milliseconds: 200));
    _chats = MockDataService.chats(count: 10);
    notifyListeners();
  }

  Future<void> loadMessages(String chatId) async {
    await Future<void>.delayed(const Duration(milliseconds: 100));
    _messagesByChat[chatId] = MockDataService.messages(chatId, count: 20);
    notifyListeners();
  }

  Future<void> sendMessage(String chatId, String text) async {
    final list = List<Message>.from(_messagesByChat[chatId] ?? const []);
    final msg = Message(
      id: 'tmp_${DateTime.now().millisecondsSinceEpoch}',
      chatId: chatId,
      senderId: 'u_1',
      text: text,
      sentAtIso: DateTime.now().toIso8601String(),
      isRead: true,
    );
    list.add(msg);
    _messagesByChat[chatId] = list;
    notifyListeners();
  }
}
