import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { Header } from '../components/organisms/Header';
import { Button } from '../components/atoms/Button';
import { usersAPI, conversationsAPI } from '../services/api';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: ${(props) => props.theme.colors.background};
`;

const Content = styled.div`
  flex: 1;
  padding: ${(props) => props.theme.spacing.large};
  display: flex;
  flex-direction: column;
  gap: ${(props) => props.theme.spacing.large};
  overflow-y: auto;
`;

const WelcomeSection = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: ${(props) => props.theme.spacing.medium};
  margin-bottom: ${(props) => props.theme.spacing.large};
`;

const Title = styled.h1`
  color: ${(props) => props.theme.colors.text};
  text-align: center;
  margin: 0;
`;

const Subtitle = styled.p`
  color: #666;
  text-align: center;
  margin: 0;
`;

const SearchSection = styled.div`
  display: flex;
  flex-direction: column;
  gap: ${(props) => props.theme.spacing.medium};
  max-width: 500px;
  width: 100%;
  align-self: center;
  background-color: ${(props) => props.theme.colors.white || '#fff'};
  padding: ${(props) => props.theme.spacing.large};
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const SearchTitle = styled.h2`
  color: ${(props) => props.theme.colors.text};
  margin: 0 0 ${(props) => props.theme.spacing.medium} 0;
  font-size: 1.2rem;
`;

const SearchForm = styled.form`
  display: flex;
  flex-direction: column;
  gap: ${(props) => props.theme.spacing.medium};
`;

const InputGroup = styled.div`
  display: flex;
  gap: ${(props) => props.theme.spacing.small};
`;

const SearchInput = styled.input`
  flex: 1;
  padding: ${(props) => props.theme.spacing.medium};
  border: 2px solid ${(props) => props.theme.colors.primary || '#007bff'};
  border-radius: 4px;
  font-size: 1rem;
  font-family: inherit;
  transition: all 0.2s ease;

  &:focus {
    outline: none;
    border-color: ${(props) => props.theme.colors.primary || '#0056b3'};
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
  }

  &::placeholder {
    color: #999;
  }
`;

const ButtonGroup = styled.div`
  display: flex;
  gap: ${(props) => props.theme.spacing.md};
  flex-direction: column;
  align-items: stretch;
`;

const UsersList = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: ${(props) => props.theme.spacing.xs};
  max-width: 1000px;
  width: 100%;
  align-self: center;
  text-align:center
`;

const UserCard = styled.div`
  background-color: ${(props) => props.theme.colors.white || '#fff'};
  padding: ${(props) => props.theme.spacing.large};
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  margin: 2.5em;

  gap: ${(props) => props.theme.spacing.small};
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
`;

const UserName = styled.h3`
  margin: 0;
  color: ${(props) => props.theme.colors.text};
  font-size: 1rem;
`;

const UserEmail = styled.p`
  margin: 0;
  color: #666;
  font-size: 0.9rem;
  word-break: break-all;
`;

const InviteButton = styled(Button)`
  width: 100%;
  font-size: 0.9rem;
`;

const LoadingText = styled.p`
  color: #666;
  text-align: center;
  font-size: 1rem;
`;

const EmptyState = styled.div`
  text-align: center;
  color: #666;
  padding: ${(props) => props.theme.spacing.large};
`;

const SearchButton = styled(Button)`
  width: 100%;
`;

export interface FriendsPageProps {
  userName: string;
  userId?: string;
  onChatClick?: () => void;
  onSettingsClick?: () => void;
  onLogout?: () => void;
  onConversationCreated?: (conversationId: string, contactName: string, contactId: string) => void;
}

interface User {
  id: string;
  email: string;
  full_name: string;
  preferred_language: string;
}

export const FriendsPage: React.FC<FriendsPageProps> = ({
  userName,
  userId,
  onChatClick,
  onSettingsClick,
  onLogout,
  onConversationCreated,
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [users, setUsers] = useState<User[]>([]);
  const [filteredUsers, setFilteredUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Récupérer les utilisateurs disponibles au chargement
  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        setError(null);
        const token = localStorage.getItem('access_token');
        if (!token) {
          throw new Error('Token not found');
        }

        const allUsers = await usersAPI.searchUsers(token);
        // Filtrer l'utilisateur courant
        const otherUsers = allUsers.filter((user) => user.id !== userId);
        setUsers(otherUsers);
        setFilteredUsers(otherUsers);
      } catch (err) {
        console.error('Error fetching users:', err);
        setError(err instanceof Error ? err.message : 'Erreur lors du chargement des utilisateurs');
        setUsers([]);
        setFilteredUsers([]);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, [userId]);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) {
      setFilteredUsers(users);
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const token = localStorage.getItem('access_token');
      if (!token) {
        throw new Error('Token not found');
      }

      const results = await usersAPI.searchUsers(token, searchQuery);
      // Filtrer l'utilisateur courant
      const otherUsers = results.filter((user) => user.id !== userId);
      setFilteredUsers(otherUsers);
    } catch (err) {
      console.error('Error searching users:', err);
      setError(err instanceof Error ? err.message : 'Erreur lors de la recherche');
      setFilteredUsers([]);
    } finally {
      setLoading(false);
    }
  };

  const handleInvite = async (user: User) => {
    try {
      setLoading(true);
      setError(null);
      const token = localStorage.getItem('access_token');
      if (!token) {
        throw new Error('Token not found');
      }

      console.log('Creating conversation with user:', user);

      // Créer une conversation privée avec cet utilisateur
      const conversation = await conversationsAPI.create(
        token,
        `${user.full_name}`,
        false, // isGroup: false pour une conversation privée
        [user.id] // ajouter l'utilisateur à la conversation
      );

      console.log('Conversation created successfully:', conversation);
      
      if (!conversation.id) {
        throw new Error('Conversation ID is missing from response');
      }
      
      setLoading(false);
      
      if (onConversationCreated) {
        console.log('Calling onConversationCreated with ID:', conversation.id, 'Contact:', user.full_name, user.id);
        onConversationCreated(conversation.id, user.full_name, user.id);
      } else {
        console.error('onConversationCreated callback not provided');
        setError('Navigation callback not available');
      }
    } catch (err) {
      console.error('Error creating conversation:', err);
      const errorMessage = err instanceof Error ? err.message : 'Erreur lors de la création de la conversation';
      setError(errorMessage);
      setLoading(false);
    }
  };

  return (
    <Container>
      <Header
        title="Mes contacts"
        onBackClick={onLogout}
        backButtonLabel="Déconnexion"
      />
      
      <Content>
        <WelcomeSection>
          <Title>👋 Bienvenue {userName}</Title>
          <Subtitle>Recherchez d'autres utilisateurs pour commencer à discuter</Subtitle>
        </WelcomeSection>

        <SearchSection>
          <SearchForm onSubmit={handleSearch}>
            <InputGroup>
              <SearchInput
                type="text"
                placeholder="Entrez un email ou un nom..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              <SearchButton type="submit">
                Chercher
              </SearchButton>
            </InputGroup>
          </SearchForm>
        </SearchSection>

        {error && (
          <EmptyState>
            <p>⚠️ {error}</p>
          </EmptyState>
        )}

        {loading ? (
          <LoadingText>...</LoadingText>
        ) : filteredUsers.length > 0 ? (
          <UsersList>
            {filteredUsers.map((user) => (
              <UserCard key={user.id}>
                <div>
                  <UserName>{user.full_name}</UserName>
                </div>
                <InviteButton onClick={() => handleInvite(user)}>
                  Discuter avec
                </InviteButton>
              </UserCard>
            ))}
          </UsersList>
        ) : (
          <EmptyState>
            <p>
              {searchQuery ? 'Cet utilisateur est introuvable' : ''}
            </p>
          </EmptyState>
        )}

        <div style={{ alignSelf: 'center', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <Button onClick={onChatClick} style={{ width: '200px' }}>
            Discussions
          </Button>
          <Button onClick={onSettingsClick} style={{ width: '200px' }}>
            Paramètres
          </Button>
        </div>
      </Content>
    </Container>
  );
};
