import 'dart:math';
import '../models/user.dart';
import '../models/influencer.dart';
import '../models/campaign.dart';
import '../models/chat.dart';
import '../models/message.dart';

class MockDataService {
  static final Random _rand = Random(42);

  static AppUser currentUser() => AppUser(
        id: 'u_1',
        fullName: 'Alex Carter',
        username: 'alexcarter',
        avatarUrl: '',
        bio: 'Creator | Tech | Lifestyle',
        followers: 12800,
        following: 615,
      );

  static List<InfluencerProfile> influencers({int count = 12}) {
    return List.generate(count, (i) {
      return InfluencerProfile(
        id: 'i_$i',
        name: 'Influencer ${i + 1}',
        username: 'influencer${i + 1}',
        avatarUrl: '',
        categories: ['Tech', if (i % 2 == 0) 'Lifestyle' else 'Beauty'],
        reach: 10000 + _rand.nextInt(100000),
        engagementRate: (_rand.nextDouble() * 0.1) + 0.02,
        ratePerPost: 50 + _rand.nextInt(500).toDouble(),
      );
    });
  }

  static List<Campaign> campaigns({int count = 8}) {
    return List.generate(count, (i) {
      return Campaign(
        id: 'c_$i',
        title: 'Campaign ${i + 1}',
        brandName: i.isEven ? 'Brandify' : 'Nova Co',
        budget: 1000 + _rand.nextInt(9000).toDouble(),
        deadlineIso: DateTime.now().add(Duration(days: 7 + i)).toIso8601String(),
        imageUrl: '',
        tags: ['Tech', 'Sponsored'],
        description: 'Work with us to promote our latest product.',
      );
    });
  }

  static List<Chat> chats({int count = 6}) {
    return List.generate(count, (i) {
      return Chat(
        id: 'chat_$i',
        participantIds: ['u_1', 'i_$i'],
        lastMessage: 'Hey there! Interested in collaboration? #${i + 1}',
      );
    });
  }

  static List<Message> messages(String chatId, {int count = 12}) {
    return List.generate(count, (i) {
      final isUser = i % 2 == 0;
      return Message(
        id: 'm_${chatId}_$i',
        chatId: chatId,
        senderId: isUser ? 'u_1' : 'i_1',
        text: isUser ? 'Sounds good to me!' : 'Can you share more details?',
        sentAtIso: DateTime.now().subtract(Duration(minutes: i * 3)).toIso8601String(),
        isRead: i < count - 2,
      );
    });
  }
}
